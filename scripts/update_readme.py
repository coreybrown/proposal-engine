#!/usr/bin/env python3
"""Keep README.md in step with the engine.

Three tiers:
  1. Auto-fix. Rewrites facts derivable from .claude/agents/*.md frontmatter wherever the README
     marks them: inline <!-- auto:KEY -->value<!-- /auto --> and the <!-- auto:model-list --> block.
  2. Fail. Structural drift a script can detect but a human must fix: agents missing from (or
     unknown to) the README's stage tables, tables that disagree with the skill files, broken links.
  3. Review. Given --changed files, lists README sections whose prose may be stale.

Usage: python3 scripts/update_readme.py [--repo DIR] [--changed FILE ...] [--check]
  --check   report only; don't rewrite README.md (exit 1 if it would change)
Exit 1 on any tier-2 failure. A README without markers is left alone.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

SKILL = {"feature": ".claude/skills/propose/SKILL.md", "new-product": ".claude/skills/propose/new-product.md"}

# Changed file (prefix) -> README sections whose prose describes it.
PROSE_MAP = [
    (".claude/skills/propose/SKILL.md", ["How it works > A run, step by step", "Stages and agents (existing product)"]),
    (".claude/skills/propose/new-product.md", ["How it works > A run, step by step", "Stages and agents (new product)", "Cost levers (early exit)"]),
    ("docs/risk-contract.md", ["A run, step by step (stage check)", "What's opinionated here"]),
    ("docs/new-product-contract.md", ["What's opinionated here > Number integrity", "A run, step by step (stage check)"]),
    ("docs/estimating.md", ["How it works > The pieces"]),
    ("docs/", ["How it works > The pieces"]),
    ("scripts/digest.py", ["A run, step by step (stage check)", "Customizing"]),
    ("scripts/extract_sources.py", ["Quick start"]),
    ("requirements.txt", ["Quick start"]),
    ("inputs/", ["Quick start"]),
    ("CLAUDE.md", ["Customizing"]),
]
MODEL_ORDER = ["opus", "sonnet", "haiku", "fable", "inherit"]


def frontmatter(path):
    lines = path.read_text().splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fm = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        key, sep, value = line.partition(":")
        if sep:
            fm[key.strip()] = value.strip()
    return fm


def load_agents(repo):
    agents = {}
    for f in sorted((repo / ".claude/agents").glob("*.md")):
        fm = frontmatter(f)
        tools = [t.strip() for t in fm.get("tools", "").split(",") if t.strip()]
        agents[f.stem] = {"model": fm.get("model", "inherit"), "tools": tools}
    return agents


def mentions(text, name):
    """The skill files name each agent they launch in bold: **name**."""
    return f"**{name}**" in text


def stage_table(readme, key):
    """Agents in the table after <!-- table:KEY -->: (core, optional). None if the marker is missing."""
    lines = readme.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if f"<!-- table:{key} -->" in l)
    except StopIteration:
        return None
    core, optional, rows = [], [], 0
    for line in lines[start + 1:]:
        if not line.startswith("|"):
            if rows:
                break
            continue
        rows += 1
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if rows <= 2 or len(cells) < 2:  # header and separator
            continue
        target = optional if "optional" in cells[0].lower() else core
        for token in re.split(r",|∥|\bthen\b", cells[1]):
            token = token.strip()
            if token and not token.startswith("`"):
                target.append(token)
    return core, optional


def model_label(model):
    return {"inherit": "Inherit (main session's model)"}.get(model, model[:1].upper() + model[1:])


def derive(agents, tables):
    facts = {"agents_total": len(agents),
             "websearch_count": sum("WebSearch" in a["tools"] for a in agents.values())}
    models = sorted({a["model"] for a in agents.values()},
                    key=lambda m: (MODEL_ORDER.index(m) if m in MODEL_ORDER else 99, m))
    for m in models:
        facts[f"{m}_count"] = sum(a["model"] == m for a in agents.values())
    for key, table in tables.items():
        if table is None:
            continue
        core = sorted(set(table[0]))
        slug = key.replace("-", "_")
        facts[f"{slug}_agents"] = len(core)
        for m in models:
            facts[f"{slug}_{m}"] = sum(agents.get(n, {}).get("model") == m for n in core)
    block = []
    for m in models:
        names = [n for n, a in agents.items() if a["model"] == m]
        block.append(f"- **{model_label(m)} ({len(names)}):** {', '.join(names)}")
    return facts, "\n".join(block)


def apply_facts(readme, facts, model_block):
    errors = []

    def inline(match):
        key = match.group(1)
        if key not in facts:
            errors.append(f"README uses unknown auto key '{key}' (known: {', '.join(sorted(facts))})")
            return match.group(0)
        return f"<!-- auto:{key} -->{facts[key]}<!-- /auto -->"

    out = re.sub(r"<!-- auto:([a-z_]+) -->.*?<!-- /auto -->", inline, readme)
    out = re.sub(r"(<!-- auto:model-list -->\n).*?(\n<!-- /auto:model-list -->)",
                 lambda m: m.group(1) + model_block + m.group(2), out, flags=re.S)
    return out, errors


def structural_checks(repo, readme, agents, tables):
    errors = []
    in_tables = set()
    for key, table in tables.items():
        if table is None:
            errors.append(f"README is missing the <!-- table:{key} --> marker before its stage table")
            continue
        named = set(table[0]) | set(table[1])
        in_tables |= named
        for name in sorted(named - set(agents)):
            errors.append(f"README {key} table names '{name}', but there is no .claude/agents/{name}.md")
        skill_path = repo / SKILL[key]
        if skill_path.exists():
            skill = skill_path.read_text()
            for name in sorted(n for n in agents if mentions(skill, n) and n not in named):
                errors.append(f"{SKILL[key]} uses '{name}', but the README {key} table doesn't list it")
            for name in sorted(n for n in named if n in agents and not mentions(skill, n)):
                errors.append(f"README {key} table lists '{name}', but {SKILL[key]} never mentions it")
    for name in sorted(set(agents) - in_tables):
        errors.append(f"agent '{name}' exists but isn't in any README stage table")
    for link in sorted(set(re.findall(r"\]\((?!https?:|#|mailto:)([^)\s]+)\)", readme))):
        if not (repo / link.split("#")[0]).exists():
            errors.append(f"README links to '{link}', which doesn't exist")
    return errors


def prose_hints(repo, changed):
    hints = {}
    for f in changed:
        for prefix, sections in PROSE_MAP:
            if f == prefix or (prefix.endswith("/") and f.startswith(prefix)):
                for s in sections:
                    hints.setdefault(s, set()).add(f)
                break
        if f.startswith(".claude/agents/") and model_changed(repo, f):
            for s in ("What it costs > Measured costs", "Cost levers (the untested-setup note)"):
                hints.setdefault(s, set()).add(f + " (model changed)")
    return hints


def model_changed(repo, path):
    diff = subprocess.run(["git", "-C", str(repo), "diff", "--cached", "-U0", "--", path],
                          capture_output=True, text=True).stdout
    return re.search(r"^[-+]model:", diff, re.M) is not None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--repo", default=".")
    ap.add_argument("--changed", nargs="*", default=[])
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)

    repo = Path(args.repo).resolve()
    readme_path = repo / "README.md"
    readme = readme_path.read_text()
    if "<!-- auto:" not in readme and "<!-- table:" not in readme:
        print("README.md has no auto markers; nothing to do.")
        return 0

    agents = load_agents(repo)
    tables = {key: stage_table(readme, key) for key in SKILL}
    facts, model_block = derive(agents, tables)
    updated, errors = apply_facts(readme, facts, model_block)
    errors += structural_checks(repo, updated, agents, tables)

    if updated != readme:
        if args.check:
            errors.append("README facts are stale; run without --check to update them")
        else:
            readme_path.write_text(updated)
            print("updated README facts: agent counts, model split and model list")
    else:
        print("README facts are current")

    hints = prose_hints(repo, args.changed)
    if hints:
        print("README prose to review by hand (the files these sections describe changed):")
        for section, files in hints.items():
            print(f"  - {section}  <- {', '.join(sorted(files))}")

    for e in errors:
        print(f"FAIL: {e}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
