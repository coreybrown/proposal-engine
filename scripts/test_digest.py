#!/usr/bin/env python3
"""Tests for scripts/digest.py --check. Run from the repo root: python3 -m unittest scripts/test_digest.py"""

import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import digest  # noqa: E402

FIGURES = """\
KEY_FIGURES:
  - name: competitor_price_low
    value: 0
    unit: usd per user per month
    kind: sourced
    source: https://apps.apple.com/example
    fetched: 2026-09-25
    {quote_line}
"""

RISKS = """\
RISKS:
  - risk: Channel reach is unproven
    severity: medium
    confidence: low
    investigate: Run a two-week paid search test
"""


def agent_file(bottom_line, quote_line='quote: "Price: Free"', risks=RISKS):
    padding = "Supporting detail for the finding, repeated so the file clears the length check.\n" * 20
    return (f"# Go-to-market\n\n## Bottom line\n{textwrap.dedent(bottom_line).strip()}\n\n## Detail\n\n{padding}\n"
            + FIGURES.format(quote_line=quote_line) + "\n" + risks)


class CheckFileTest(unittest.TestCase):
    def check(self, text):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "go-to-market.md"
            path.write_text(text, encoding="utf-8")
            return digest.check_file(path)

    def test_kill_marker_flags(self):
        errs, _, flags = self.check(agent_file("- **KILL:** no channel reaches roofers at a CAC under $40"))
        self.assertEqual(errs, [])
        self.assertEqual(flags, ["KILL"])

    def test_kill_marker_variants_flag(self):
        for line in ("KILL: no channel", "- KILL: no channel", "* **KILL**: no channel", "  - __KILL:__ no channel"):
            with self.subTest(line=line):
                self.assertEqual(self.check(agent_file(line))[2], ["KILL"])

    def test_negated_kill_does_not_flag(self):
        errs, warns, flags = self.check(agent_file("""
            - **Finding:** Paid search reaches the segment. Not a KILL: CAC sits under the ceiling.
        """))
        self.assertEqual(errs, [])
        self.assertEqual(flags, [])
        self.assertTrue(any("'KILL:' mid-line" in w for w in warns), warns)

    def test_needs_input_marker(self):
        self.assertEqual(self.check(agent_file("- **NEEDS INPUT:** the builder's budget"))[2], ["NEEDS INPUT"])
        _, _, flags = self.check(agent_file("- **Finding:** no NEEDS INPUT: all data was public"))
        self.assertEqual(flags, [])

    def test_text_after_quote_names_entry_and_fix(self):
        errs, _, _ = self.check(agent_file(
            "- **Finding:** fine",
            quote_line='quote: "Price: Free" (App Store listing; no in-app purchases found)'))
        self.assertEqual(len(errs), 1, errs)
        self.assertIn("KEY_FIGURES block does not parse", errs[0])
        self.assertIn("'competitor_price_low'", errs[0])
        self.assertIn("note:", errs[0])

    def test_note_field_passes(self):
        errs, _, _ = self.check(agent_file(
            "- **Finding:** fine",
            quote_line='quote: "Price: Free"\n    note: App Store listing; no in-app purchases found'))
        self.assertEqual(errs, [])

    def test_unquoted_colon_in_figure_names_entry_and_fix(self):
        errs, _, _ = self.check(agent_file(
            "- **Finding:** fine",
            quote_line='quote: "Price: Free"\n    note: seen on the listing: no in-app purchases'))
        self.assertEqual(len(errs), 1, errs)
        self.assertIn("'competitor_price_low'", errs[0])
        self.assertIn("unquoted value contains ': '", errs[0])
        self.assertIn("note: >-", errs[0])

    def test_unquoted_colon_in_risk_names_entry_and_fix(self):
        risks = RISKS.replace("Run a two-week paid search test", "Run a paid search test; owner: growth")
        errs, _, _ = self.check(agent_file("- **Finding:** fine", risks=risks))
        self.assertEqual(len(errs), 1, errs)
        self.assertIn("RISKS block does not parse", errs[0])
        self.assertIn("'- risk: Channel reach is unproven'", errs[0])
        self.assertIn("investigate: >-", errs[0])

    def test_folded_block_with_colons_and_quotes_passes(self):
        risks = textwrap.dedent("""\
            RISKS:
              - risk: >-
                  The demo's "Opens on launch" control contradicts the spec: it persists state.
                severity: medium
                confidence: high
                investigate: >-
                  Remove the control from the demo; owner: prototyper
        """)
        errs, _, _ = self.check(agent_file("- **Finding:** fine", risks=risks))
        self.assertEqual(errs, [])

    def test_folded_block_body_is_not_blamed(self):
        # The investigate line is the real error; the folded risk body only looks like `key: a: b`.
        risks = textwrap.dedent("""\
            RISKS:
              - risk: >-
                  Owner: growth: the channel is unproven
                severity: medium
                confidence: low
                investigate: Test it; owner: growth
        """)
        errs, _, _ = self.check(agent_file("- **Finding:** fine", risks=risks))
        self.assertEqual(len(errs), 1, errs)
        self.assertIn("investigate: Test it", errs[0])


if __name__ == "__main__":
    unittest.main()
