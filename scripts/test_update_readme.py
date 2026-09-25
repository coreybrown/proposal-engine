#!/usr/bin/env python3
"""Tests for scripts/update_readme.py. Run from the repo root: python3 scripts/test_update_readme.py"""

import io
import sys
import tempfile
import textwrap
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import update_readme  # noqa: E402

README = textwrap.dedent("""\
    # Test
    We ship <!-- auto:agents_total -->1<!-- /auto --> agents, <!-- auto:opus_count -->9<!-- /auto --> on Opus.

    **Existing product (<!-- auto:feature_agents -->0<!-- /auto --> agents)**
    <!-- table:feature -->

    | Stage | Agents | Output |
    |---|---|---|
    | 1. Context | alpha, beta | x |

    **New product**
    <!-- table:new-product -->

    | Stage | Agents | Output |
    |---|---|---|
    | 0. Ingest | `scripts/x.py` | x |
    | 1. Frame | gamma | x |
    | 6. Optional | delta | x |

    <!-- auto:model-list -->
    old
    <!-- /auto:model-list -->

    See [the docs](docs/).
    """)


def agent(model, tools="Read, Write"):
    return f"---\nname: x\ntools: {tools}\nmodel: {model}\n---\nBody\n"


class UpdateReadmeTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        (self.repo / ".claude/agents").mkdir(parents=True)
        (self.repo / ".claude/skills/propose").mkdir(parents=True)
        (self.repo / "docs").mkdir()
        for name, model in [("alpha", "opus"), ("beta", "sonnet"), ("gamma", "opus"), ("delta", "sonnet")]:
            (self.repo / f".claude/agents/{name}.md").write_text(agent(model, "Read, WebSearch"))
        (self.repo / ".claude/skills/propose/SKILL.md").write_text("Launch **alpha** and **beta**.")
        (self.repo / ".claude/skills/propose/new-product.md").write_text("Launch **gamma**. Stage 6: **delta**.")
        (self.repo / "README.md").write_text(README)

    def tearDown(self):
        self.tmp.cleanup()

    def run_it(self, *args):
        out = io.StringIO()
        with redirect_stdout(out):
            code = update_readme.main(["--repo", str(self.repo), *args])
        return code, out.getvalue(), (self.repo / "README.md").read_text()

    def test_rewrites_stale_facts(self):
        code, _, readme = self.run_it()
        self.assertEqual(code, 0)
        self.assertIn("<!-- auto:agents_total -->4<!-- /auto -->", readme)
        self.assertIn("<!-- auto:opus_count -->2<!-- /auto -->", readme)
        self.assertIn("<!-- auto:feature_agents -->2<!-- /auto -->", readme)
        self.assertIn("- **Opus (2):** alpha, gamma", readme)
        self.assertNotIn("old", readme)

    def test_check_mode_reports_stale_without_writing(self):
        code, out, readme = self.run_it("--check")
        self.assertEqual(code, 1)
        self.assertIn("stale", out)
        self.assertEqual(readme, README)

    def test_agent_missing_from_tables_fails(self):
        (self.repo / ".claude/agents/epsilon.md").write_text(agent("sonnet"))
        code, out, _ = self.run_it()
        self.assertEqual(code, 1)
        self.assertIn("'epsilon' exists but isn't in any README stage table", out)

    def test_skill_agent_missing_from_table_fails(self):
        (self.repo / ".claude/skills/propose/SKILL.md").write_text("Launch **alpha**, **beta** and **gamma**.")
        code, out, _ = self.run_it()
        self.assertEqual(code, 1)
        self.assertIn("uses 'gamma', but the README feature table doesn't list it", out)

    def test_plain_word_in_skill_is_not_an_agent_mention(self):
        (self.repo / ".claude/skills/propose/SKILL.md").write_text("Launch **alpha** and **beta**; tell the gamma team.")
        code, _, _ = self.run_it()
        self.assertEqual(code, 0)

    def test_table_names_unknown_agent_fails(self):
        (self.repo / ".claude/agents/beta.md").unlink()
        code, out, _ = self.run_it()
        self.assertEqual(code, 1)
        self.assertIn("names 'beta', but there is no .claude/agents/beta.md", out)

    def test_broken_link_fails(self):
        (self.repo / "docs").rmdir()
        code, out, _ = self.run_it()
        self.assertEqual(code, 1)
        self.assertIn("links to 'docs/'", out)

    def test_unknown_auto_key_fails(self):
        readme = README + "\n<!-- auto:nonsense -->1<!-- /auto -->\n"
        (self.repo / "README.md").write_text(readme)
        code, out, _ = self.run_it()
        self.assertEqual(code, 1)
        self.assertIn("unknown auto key 'nonsense'", out)

    def test_prose_hints_for_changed_files(self):
        code, out, _ = self.run_it("--changed", ".claude/skills/propose/new-product.md", "docs/foo.md")
        self.assertEqual(code, 0)
        self.assertIn("Stages and agents (new product)", out)
        self.assertIn("How it works > The pieces  <- docs/foo.md", out)

    def test_readme_without_markers_is_left_alone(self):
        (self.repo / "README.md").write_text("# Plain\n")
        code, out, readme = self.run_it()
        self.assertEqual(code, 0)
        self.assertIn("no auto markers", out)
        self.assertEqual(readme, "# Plain\n")


if __name__ == "__main__":
    unittest.main()
