#!/usr/bin/env python3
"""Stage checks and the run digest for new-product runs of /propose.

Usage:
    python3 scripts/digest.py --check <run_dir> [<file> ...]
        Checks each file (relative to run_dir) against docs/new-product-contract.md.
        With no files given, checks every research/*.md plus business-case.md.
        Each file must have:
          - a Bottom line near the top
          - a KEY_FIGURES block where every figure has a valid kind
          - a RISKS block that parses
        It also reports KILL / NEEDS INPUT flags. Exits 1 if any file fails.

    python3 scripts/digest.py <run_dir>
        Writes <run_dir>/research/_digest.md. It contains:
          - every Bottom line
          - the framer's assumption and question-routing tables
          - every KEY_FIGURES entry, side by side by name
          - the drift check (the business case vs. Stage 2 evidence)
          - every RISKS block, verbatim
"""

import datetime
import re
import sys
import textwrap
from pathlib import Path

import yaml

KINDS = {"sourced", "derived", "estimate", "unknown"}
MISSING = object()

# (file, agent, stage) in pipeline order.
KNOWN_FILES = [
    ("research/opportunity-model.md", "opportunity-framer", 1),
    ("research/problem.md", "problem-validator", 2),
    ("research/market-size.md", "market-sizer", 2),
    ("research/competition.md", "competitive-strategist", 2),
    ("research/go-to-market.md", "gtm-researcher", 2),
    ("research/build-and-run.md", "build-cost-analyst", 2),
    ("research/regulatory.md", "regulatory-scout", 2),
    ("business-case.md", "venture-strategist", 3),
    ("research/risk-economics.md", "unit-economics-auditor", 4),
    ("research/risk-fact-check.md", "fact-checker", 4),
    ("research/risk-regulatory.md", "regulatory-scout (audit)", 4),
    ("research/risk-ethics-trust-safety.md", "ethics-trust-safety", 4),
    ("research/smoke-test-manifest.md", "smoke-test-builder", 6),
]

# Direction in which a core figure flatters the case. Decisions (price) and
# context (competitor prices) are not drift-checked.
FAVORABLE_HIGH = {"total_customers", "serviceable_customers", "obtainable_customers", "market_value_total",
                  "market_value_serviceable", "market_value_obtainable", "gross_margin", "cac_ceiling",
                  "breakeven_churn_monthly"}
FAVORABLE_LOW = {"cost_to_serve_per_unit", "human_minutes_per_unit", "fixed_costs_monthly", "cac",
                 "payback_months", "breakeven_customers", "build_cost_mvp", "build_weeks_mvp", "build_person_days_mvp",
                 "capital_to_breakeven"}

HEADING = re.compile(r"^(#{1,6})\s")
BOTTOM_LINE = r"^\s*#{1,6}\s*\**bottom line\**\s*:?\s*$"
FENCE = re.compile(r"^\s*```")
# A flag fires only when a Bottom line item opens with the marker: "- **KILL:** ...", not "Not a KILL: ...".
FLAG_MARKERS = {flag: re.compile(rf"^\s*(?:[-*+]\s+)?(?:\*\*|__)?{flag}(?:\*\*|__)?\s*:")
                for flag in ("KILL", "NEEDS INPUT")}
# The two usual reasons a block fails to parse, each with its fix.
YAML_PITFALLS = [
    (re.compile(r"""^\s*(?:-\s+)?[A-Za-z_]\w*:\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^']|'')*')\s*[^\s#]"""),
     "text after a closing quote in `{line}`. End the value at its closing quote and move the rest to a `note:` "
     "field, or write the whole value as a folded block (`{key}: >-`, then the text indented on the next line)"),
    (re.compile(r"""^\s*(?:-\s+)?[A-Za-z_]\w*:[ \t]+(?!["'|>\[{&*!%@`])[^#]*?:(?:\s|$)"""),
     "unquoted value contains ': ' in `{line}`. Write it as a folded block: `{key}: >-`, then the text indented "
     "on the next line"),
]


# ---------- parsing ----------

def find_block(lines, key):
    """Return (start, end) of the last `KEY:` block, or None. end is exclusive."""
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith(f"{key}:"):
            start = i
    if start is None:
        return None
    end = start + 1
    while end < len(lines):
        stripped = lines[end].strip()
        if FENCE.match(lines[end]) or HEADING.match(stripped) or stripped.startswith(("KEY_FIGURES:", "RISKS:")):
            break
        end += 1
    return start, end


def parse_block(lines, span, key):
    text = textwrap.dedent("\n".join(lines[span[0]:span[1]]))
    data = yaml.safe_load(text)
    return data.get(key) if isinstance(data, dict) else None


def entry_label(block, i):
    """Name the list entry that block line i belongs to: its `name:` if it has one, else its first line."""
    start = next((j for j in range(i, -1, -1) if re.match(r"^\s*-\s", block[j])), None)
    if start is None:
        return None
    end = next((j for j in range(start + 1, len(block)) if re.match(r"^\s*-\s", block[j])), len(block))
    for line in block[start:end]:
        match = re.match(r"^\s*(?:-\s+)?name:\s*(\S.*)$", line)
        if match:
            return f"'{match.group(1).strip()}'"
    first = " ".join(block[start].split())
    return f"'{clip(first, 60)}'"


def clip(text, width):
    text = " ".join(str(text).split())
    return (text[:width] + "…") if len(text) > width else text


def yaml_errors(key, lines, span, exc):
    """Explain why a KEY_FIGURES or RISKS block failed to parse: which line, which entry, and the fix."""
    block = lines[span[0]:span[1]]
    errs = []
    scalar_indent = None  # inside a `key: >-` or `key: |` body, where anything goes
    for i, line in enumerate(block):
        indent = len(line) - len(line.lstrip())
        if scalar_indent is not None and (not line.strip() or indent > scalar_indent):
            continue
        scalar_indent = indent if re.search(r":\s*[>|][-+]?\s*$", line) else None
        for pattern, advice in YAML_PITFALLS:
            if pattern.match(line):
                label = entry_label(block, i)
                where = f"line {span[0] + i + 1}" + (f", entry {label}" if label else "")
                field = line.split(":", 1)[0].strip().lstrip("- ")
                errs.append(f"{key} block does not parse as YAML ({where}): "
                            + advice.format(line=clip(line, 100), key=field))
                break
    if errs:
        return errs
    mark = getattr(exc, "problem_mark", None)
    if mark is None or mark.line >= len(block):
        return [f"{key} block does not parse as YAML: {' '.join(str(exc).split())}"]
    label = entry_label(block, mark.line)
    where = f"line {span[0] + mark.line + 1}" + (f", entry {label}" if label else "")
    problem = getattr(exc, "problem", None) or str(exc).splitlines()[0]
    return [f"{key} block does not parse as YAML ({where}): {problem}, at `{clip(block[mark.line], 100)}`"]


def find_section(lines, title_pattern, within=None):
    """Return (heading_index, end) of the first heading matching title_pattern."""
    limit = len(lines) if within is None else min(within, len(lines))
    for i in range(limit):
        match = HEADING.match(lines[i].strip())
        if match and re.search(title_pattern, lines[i], re.I):
            level = len(match.group(1))
            end = i + 1
            while end < len(lines):
                other = HEADING.match(lines[end].strip())
                if other and len(other.group(1)) <= level:
                    break
                end += 1
            return i, end
    return None


def bottom_line_body(lines, span):
    """Lines of the Bottom line section, stopping at any figures, risks, fence or rule."""
    body = []
    for line in lines[span[0] + 1:span[1]]:
        stripped = line.strip()
        if stripped.startswith(("KEY_FIGURES:", "RISKS:", "```", "---")):
            break
        body.append(line)
    return body


def parse_number(value):
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        s = value.strip().lower().replace(",", "").replace("$", "").replace("usd", "").strip()
        percent = s.endswith("%")
        s = s.rstrip("%").strip()
        try:
            number = float(s)
        except ValueError:
            return None
        return number / 100 if percent else number
    return None


def norm_unit(unit):
    s = str(unit or "").lower().replace("/", " per ").replace("$", "usd ")
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", s).split())


# ---------- checks ----------

def check_figure(fig):
    if not isinstance(fig, dict):
        return ["a KEY_FIGURES entry is not a mapping"]
    errs = []
    name = fig.get("name")
    label = name or "(unnamed)"
    if not name or not re.fullmatch(r"[a-z][a-z0-9_]*", str(name)):
        errs.append(f"{label}: name is missing or not snake_case")
    kind = fig.get("kind")
    if kind is None:
        errs.append(f"{label}: has no kind (must be sourced / derived / estimate / unknown)")
    elif kind not in KINDS:
        errs.append(f"{label}: kind {kind!r} is not one of sourced / derived / estimate / unknown")
    if not fig.get("unit"):
        errs.append(f"{label}: unit is missing")
    value = fig.get("value", MISSING)
    if kind in KINDS - {"unknown"} and parse_number(value) is None:
        errs.append(f"{label}: value must be one number, the conservative one (got {value if value is not MISSING else 'nothing'!r})")
    if kind == "sourced":
        source = str(fig.get("source") or "")
        if not source:
            errs.append(f"{label}: sourced figure has no source")
        if not fig.get("quote"):
            errs.append(f"{label}: sourced figure has no quote from the source")
        if source.startswith("http") and not fig.get("fetched"):
            errs.append(f"{label}: web source has no fetched date")
        # Uploads are local paths; a web URL like .../resources/ is not an upload.
        from_upload = not source.startswith("http") and re.search(r"(?<![\w.-])(sources|materials)/", source)
        if from_upload and fig.get("asserted") is not True:
            errs.append(f"{label}: figure from uploaded material must carry asserted: true")
    elif kind == "derived" and not fig.get("formula"):
        errs.append(f"{label}: derived figure has no formula")
    elif kind == "estimate":
        if not fig.get("reasoning"):
            errs.append(f"{label}: estimate shows no reasoning")
        if not fig.get("replace_with"):
            errs.append(f"{label}: estimate does not name the data that would replace it (replace_with)")
    elif kind == "unknown":
        if not fig.get("settle_with"):
            errs.append(f"{label}: unknown does not say what would settle it (settle_with)")
        if value not in (None, MISSING):
            errs.append(f"{label}: unknown figure must have value: null")
    return errs


def check_risks(lines):
    span = find_block(lines, "RISKS")
    if span is None:
        return ["no RISKS: block"], None
    first = lines[span[0]].strip()
    if re.match(r"RISKS:\s*none identified", first, re.I):
        after = re.sub(r"(?i)RISKS:\s*none identified", "", first).strip(" .:-#")
        following = [l for l in lines[span[0] + 1:span[0] + 4] if l.strip() and not FENCE.match(l)]
        if not after and not following:
            return ["'RISKS: none identified' must be followed by one sentence on what was checked"], span
        return [], span
    try:
        risks = parse_block(lines, span, "RISKS")
    except yaml.YAMLError as exc:
        return yaml_errors("RISKS", lines, span, exc), span
    if not isinstance(risks, list) or not risks:
        return ["RISKS block is empty or not a list"], span
    errs = []
    for n, risk in enumerate(risks, 1):
        if not isinstance(risk, dict):
            errs.append(f"risk {n}: not a mapping")
            continue
        for key in ("risk", "severity", "confidence", "investigate"):
            if not risk.get(key):
                errs.append(f"risk {n}: missing {key}")
        for key in ("severity", "confidence"):
            if risk.get(key) and str(risk[key]).strip().lower() not in ("high", "medium", "low"):
                errs.append(f"risk {n}: {key} {risk[key]!r} is not high / medium / low")
    return errs, span


def read_figures(lines):
    """Return (figures, errors, span). figures is [] for KEY_FIGURES: none."""
    span = find_block(lines, "KEY_FIGURES")
    if span is None:
        return [], ["no KEY_FIGURES: block (write 'KEY_FIGURES: none' if the file uses no figures)"], None
    if re.match(r"KEY_FIGURES:\s*none", lines[span[0]].strip(), re.I):
        return [], [], span
    try:
        figures = parse_block(lines, span, "KEY_FIGURES")
    except yaml.YAMLError as exc:
        return [], yaml_errors("KEY_FIGURES", lines, span, exc), span
    if not isinstance(figures, list):
        return [], ["KEY_FIGURES block is not a list (or 'KEY_FIGURES: none')"], span
    errs = [e for fig in figures for e in check_figure(fig)]
    return [f for f in figures if isinstance(f, dict)], errs, span


def check_file(path):
    """Return (errors, warnings, flags) for one agent output file."""
    if not path.exists():
        return ["file is missing"], [], []
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    errs, warns, flags = [], [], []
    if len(text) < 1500:
        errs.append(f"file is suspiciously short ({len(text)} characters): the agent may have failed or been cut off")
    bottom = find_section(lines, BOTTOM_LINE, within=60)
    if bottom is None:
        errs.append("no '## Bottom line' section near the top")
    else:
        body = [l for l in bottom_line_body(lines, bottom) if l.strip()]
        if len(body) > 7:
            warns.append(f"Bottom line runs {len(body)} lines (the contract allows 5)")
        for flag, marker in FLAG_MARKERS.items():
            if any(marker.match(l) for l in body):
                flags.append(flag)
            elif any(f"{flag}:" in l for l in body):
                warns.append(f"Bottom line mentions '{flag}:' mid-line, so it does not fire; the marker is reserved "
                             f"for firing, so reword it")
    _, figure_errs, figure_span = read_figures(lines)
    errs += figure_errs
    risk_errs, risk_span = check_risks(lines)
    errs += risk_errs
    if figure_span and risk_span and figure_span[0] > risk_span[0]:
        warns.append("KEY_FIGURES should come immediately before RISKS")
    return errs, warns, flags


def run_check(run_dir, names):
    if not names:
        names = [f for f, _, _ in KNOWN_FILES if (run_dir / f).exists()]
        names += sorted(str(p.relative_to(run_dir)) for p in (run_dir / "research").glob("*.md")
                        if not p.name.startswith("_") and str(p.relative_to(run_dir)) not in names)
    failed = False
    for name in names:
        errs, warns, flags = check_file(run_dir / name)
        status = "FAIL" if errs else "PASS"
        failed |= bool(errs)
        extra = f" [{', '.join(flags)}]" if flags else ""
        print(f"{name}: {status}{extra}")
        for e in errs:
            print(f"  - {e}")
        for w in warns:
            print(f"  ~ {w}")
    return 1 if failed else 0


# ---------- digest ----------

def drift_check(figures_by_file):
    """Compare business-case figures with the most conservative Stage 2 value."""
    stage2 = [(f, fig) for f, agent, stage in KNOWN_FILES if stage == 2 for fig in figures_by_file.get(f, [])]
    stage2_sources = {str(fig.get("source")) for _, fig in stage2 if fig.get("source")}
    hits, notes = [], []
    for fig in figures_by_file.get("business-case.md", []):
        name = fig.get("name")
        if name not in FAVORABLE_HIGH | FAVORABLE_LOW:
            continue
        value = parse_number(fig.get("value"))
        if value is None:
            continue
        candidates = [(f, g) for f, g in stage2 if g.get("name") == name and parse_number(g.get("value")) is not None]
        if not candidates:
            notes.append(f"`{name}`: no Stage 2 value to compare against")
            continue
        same_unit = [(f, g) for f, g in candidates if norm_unit(g.get("unit")) == norm_unit(fig.get("unit"))]
        if not same_unit:
            units = ", ".join(sorted({str(g.get('unit')) for _, g in candidates}))
            notes.append(f"`{name}`: units differ (business case: {fig.get('unit')}; Stage 2: {units}); compare by hand")
            continue
        pick = min if name in FAVORABLE_HIGH else max
        src_file, conservative = pick(same_unit, key=lambda fg: parse_number(fg[1].get("value")))
        base = parse_number(conservative.get("value"))
        flatters = value > base if name in FAVORABLE_HIGH else value < base
        if not flatters:
            continue
        pct = f" ({abs(value - base) / abs(base):.0%} more favorable)" if base else ""
        line = (f"`{name}`: business case uses {fig.get('value')} {fig.get('unit')} ({fig.get('kind')}) vs. the most "
                f"conservative Stage 2 value {conservative.get('value')} {conservative.get('unit')} from `{src_file}`{pct}")
        new_source = fig.get("kind") == "sourced" and str(fig.get("source")) not in stage2_sources
        if new_source:
            notes.append(f"{line}. It cites a new source ({fig.get('source')}): the fact-checker must verify it")
        else:
            hits.append(f"**DRIFT** {line}, and cites no new source")
    return hits, notes


def fmt_basis(fig):
    for key in ("source", "formula", "reasoning", "settle_with"):
        if fig.get(key):
            return clip(fig[key], 140)
    return ""


def write_digest(run_dir):
    present = [(f, a, s) for f, a, s in KNOWN_FILES if (run_dir / f).exists()]
    extra = sorted(p for p in (run_dir / "research").glob("*.md")
                   if not p.name.startswith("_") and str(p.relative_to(run_dir)) not in {f for f, _, _ in KNOWN_FILES})
    present += [(str(p.relative_to(run_dir)), "other", 0) for p in extra]

    figures_by_file, sections = {}, {}
    compliance, bottoms, risks = [], [], []
    for name, agent, _ in present:
        lines = (run_dir / name).read_text(encoding="utf-8", errors="replace").splitlines()
        errs, warns, flags = check_file(run_dir / name)
        status = "FAIL: " + "; ".join(errs) if errs else "pass"
        if flags:
            status += f" [{', '.join(flags)}]"
        compliance.append(f"| `{name}` | {agent} | {status} |")
        figures, _, _ = read_figures(lines)
        figures_by_file[name] = figures
        bottom = find_section(lines, BOTTOM_LINE, within=60)
        body = "\n".join(bottom_line_body(lines, bottom)).strip() if bottom else "_(no Bottom line)_"
        bottoms.append(f"### {agent}: `{name}`\n\n{body}")
        _, span = check_risks(lines)
        block = "\n".join(lines[span[0]:span[1]]).rstrip() if span else "(no RISKS block)"
        risks.append(f"### {agent}: `{name}`\n\n```yaml\n{textwrap.dedent(block)}\n```")
        if name == "research/opportunity-model.md":
            for key, pattern in (("assumptions", r"what must be true"), ("routing", r"question routing")):
                sec = find_section(lines, pattern)
                if sec:
                    sections[key] = "\n".join(lines[sec[0] + 1:sec[1]]).strip()

    by_name = {}
    for name, agent, _ in present:
        for fig in figures_by_file[name]:
            by_name.setdefault(str(fig.get("name")), []).append((name, agent, fig))
    figure_md = []
    for fig_name in sorted(by_name):
        rows = [f"| `{f}` | {a} | {g.get('value')} | {g.get('unit', '')} | {g.get('kind')} | {fmt_basis(g)} |"
                for f, a, g in by_name[fig_name]]
        figure_md.append(f"### {fig_name}\n\n| File | Agent | Value | Unit | Kind | Source / formula / reasoning |\n"
                         f"|---|---|---|---|---|---|\n" + "\n".join(rows))

    hits, notes = drift_check(figures_by_file)
    drift_md = hits or ["No drift found: no business-case figure is more favorable than the Stage 2 evidence."]
    if "business-case.md" not in figures_by_file:
        drift_md = ["Not run yet: there is no business case."]

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    out = [f"# Run digest: {run_dir.name}", "",
           f"Generated {now} by `scripts/digest.py`. Everything below is copied verbatim from the files listed. "
           "Read this instead of every file; open a file only to settle a specific question.", "",
           "## Compliance", "", "| File | Agent | Stage check |", "|---|---|---|", *compliance, "",
           "## Bottom lines", "", *[b + "\n" for b in bottoms],
           "## What must be true (from opportunity-model.md)", "", sections.get("assumptions", "_(not found)_"), "",
           "## Question routing (from opportunity-model.md)", "", sections.get("routing", "_(not found)_"), "",
           "## Drift check", "", *[f"- {h}" for h in drift_md], ""]
    if notes:
        out += ["Also noted:", "", *[f"- {n}" for n in notes], ""]
    figure_blocks = [f + "\n" for f in figure_md] or ["_(no figures)_\n"]
    out += ["## Figures by name", "", *figure_blocks, "## RISKS blocks", "", *[r + "\n" for r in risks]]
    target = run_dir / "research" / "_digest.md"
    target.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {target} ({len(present)} files, {sum(len(v) for v in figures_by_file.values())} figures, "
          f"{len(hits)} drift hit(s))")
    return 0


def main(argv):
    if len(argv) >= 3 and argv[1] == "--check":
        return run_check(Path(argv[2]), argv[3:])
    if len(argv) == 2 and not argv[1].startswith("-"):
        return write_digest(Path(argv[1]))
    print(__doc__.strip())
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
