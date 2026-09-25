---
status: empty
---

# Team profile

This file describes the real product delivery team: who is on it, how it builds and ships, and how much it uses AI. When it is filled in, pipeline agents work in that team's context instead of from generic defaults. The team owns and edits these files directly, and they change rarely.

**While `status: empty`, agents stop reading here.** Estimates then use the default team in [../estimating.md](../estimating.md). Once the sections below are filled in, set `status: filled`.

---

## 1. Who is on the team

| Role | People | FTE on new work | Seniority | Role file |
|---|---|---|---|---|
| Product manager | | | | [roles/product-manager.md](roles/product-manager.md) |
| Product designer | | | | [roles/designer.md](roles/designer.md) |
| Front-end engineer | | | | [roles/frontend-engineer.md](roles/frontend-engineer.md) |
| Back-end engineer | | | | [roles/backend-engineer.md](roles/backend-engineer.md) |
| Mobile engineer | | | | [roles/mobile-engineer.md](roles/mobile-engineer.md) |
| QA | | | | [roles/qa.md](roles/qa.md) |
| Data / analytics | | | | [roles/data-analytics.md](roles/data-analytics.md) |

- **FTE on new work** is time left after maintenance, support and on-call. For example, 4 engineers who spend 30% on keeping the lights on count as 2.8.
- Delete rows for roles the team doesn't have. Add rows for roles it does have, such as a tech lead, content designer or ML engineer, with a role file if they have standards.

## 2. Stack

Languages, frameworks, platforms (web, iOS, Android), hosting and infrastructure, CI/CD, and the main third-party services already in use.

## 3. How the team ships

- **Cadence:** sprint length, and how planning works.
- **Definition of done:** code review rules, test coverage expectations, QA gates, accessibility checks.
- **Release:** feature flags, release trains, staged rollout, app-store review, change approval.
- **What usually slows delivery down:** dependencies on other teams, environments, approvals.

## 4. AI adoption

- **Tools** in use, and what each is used for. Examples: AI coding assistants, agentic coding, AI code review, AI-generated tests, design tools.
- **Scenario this maps to** in [../estimating.md](../estimating.md): AI-leveraged, AI-typical or traditional. This becomes the suggested estimate.
- **Where AI isn't used, and why.** Policy, security or quality reasons.

## 5. Estimate calibration

Recent work with its estimate and its actual result. Three to five rows is enough to start.

| Feature | Estimated (person-days or weeks) | Actual | Team size | AI used? | What drove the gap |
|---|---|---|---|---|---|

## 6. Partner functions

Teams outside the delivery team that the work depends on. Their turnaround times are the waits in [../estimating.md](../estimating.md) §6.

| Function | Who / how to engage | Typical turnaround |
|---|---|---|
| Legal / compliance | | |
| Security review | | |
| Support / operations | | |
| Brand / marketing | | |

## 7. Which agents apply each role

When a role file is filled in, these agents read it and apply its standards. Agents not listed here read only this README.

| Role file | Feature runs | New-product runs |
|---|---|---|
| product-manager | product-analyst, product-manager, business-viability, competitive-researcher, user-researcher, synthesizer | opportunity-framer, problem-validator, market-sizer, competitive-strategist, gtm-researcher, venture-strategist, unit-economics-auditor, new-product-synthesizer |
| designer | design-language-analyst, product-designer, prototyper, accessibility | smoke-test-builder |
| frontend-engineer | prototyper, tech-architect, accessibility | build-cost-analyst, smoke-test-builder |
| backend-engineer | tech-architect, privacy-security, operational-readiness | build-cost-analyst |
| mobile-engineer | tech-architect, prototyper | build-cost-analyst |
| qa | tech-architect, accessibility, operational-readiness | build-cost-analyst |
| data-analytics | product-manager, tech-architect, privacy-security | market-sizer, unit-economics-auditor |

Sections 1–5 of this README go to every agent that estimates effort: tech-architect and build-cost-analyst. Section 6 goes to legal-compliance, regulatory-scout, privacy-security and operational-readiness.
