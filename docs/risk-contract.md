# Shared risk contract

Every agent in the pipeline ends its written output with a `RISKS:` block in exactly this format. The synthesizer assembles the risk register mechanically from these blocks — deviations break the pipeline.

## Format

```yaml
RISKS:
  - risk: >-
      <one sentence stating the risk concretely — name the mechanism, not a vibe>
    severity: high | medium | low
    confidence: high | medium | low
    investigate: >-
      <the specific next step, and which team/role owns the answer>
```

If no risks were found:

```yaml
RISKS: none identified
# followed by one sentence stating what was actually checked
```

### YAML rules

The block must parse as YAML. Two mistakes cause almost every failure:

- **A colon followed by a space inside an unquoted value.** `investigate: Re-test the flow; owner: design` does not parse, because YAML reads `owner:` as a new key. Write prose values as folded blocks, as in the template: `>-` after the key, then the text on the next line, indented. A folded block needs no escaping for colons, quotes or `#`.
- **Text after a closing quote.** `risk: "Opens on launch" is unlabeled` does not parse. Use a folded block.

```yaml
# Wrong
    investigate: Ask 5-10 Pros whether they'd accept this flow — owner: Pro success
# Right
    investigate: >-
      Ask 5-10 Pros whether they'd accept this flow — owner: Pro success
```

## Definitions

**Severity** — impact if the risk materializes:
- `high` — could kill the feature, cause legal/safety/reputational harm, or require rework of the core approach
- `medium` — would materially change scope, cost, or timeline
- `low` — worth knowing; fixable within normal iteration

**Confidence** — how sure the agent is the risk is real:
- `high` — grounded in direct evidence (the product, the spec, a regulation, a competitor)
- `medium` — reasoned inference from partial evidence
- `low` — plausible concern the agent could not verify with available inputs

Severity and confidence are independent. A `high`-severity / `low`-confidence risk is a legitimate and useful entry — it says "if this is true it's fatal; verify it first."

**Investigate** — must name (a) a concrete action and (b) an owner. Good: "Confirm with legal whether stored location traces qualify as sensitive data under GDPR Art. 9." Bad: "Look into privacy."

## Team context

[docs/team/README.md](team/README.md) describes the real delivery team, when one has been set up.
- **Read only its first 3 lines first.** If they say `status: empty`, the profile doesn't exist yet. Use your normal defaults, including [estimating.md](estimating.md) for effort, and read no further.
- **If `status: filled`,** read the README and, from its §7 table, the role files mapped to your agent name whose own status is `filled`. Apply their standards, stack and process as constraints on what you propose. Say which files you applied.
- **New-product runs use the profile only when this team would build the product.** `idea.md` or the framer's builder context has to say so. Otherwise ignore it.
- **In feature runs, name real owners.** When the profile names roles, use them as `investigate` owners instead of generic teams.

## License to kill

Every agent is explicitly licensed to conclude negatively:

- A researcher may report "nothing differentiating found."
- A viability agent may report "this serves users but not the business."
- The ethics agent may report "this feature is a dark pattern as specced."
- The synthesizer may recommend **kill** or **do not advance without X**.

Professional hedging that buries a fatal problem under "considerations" is a contract violation. If an agent believes the honest severity of a finding is `high`, it says so in the first line of the finding, not the last.
