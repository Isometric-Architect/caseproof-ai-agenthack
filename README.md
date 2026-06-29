# CaseProof AI

Human-review governor for high-value refund exception cases in UiPath Maestro.

## Project Description

CaseProof AI is a human-review governor for AI-prepared high-value refund exception cases. It checks whether a case has enough evidence, required milestones, policy alignment, subject binding, and public-safe redaction before a person reviews it.

The problem it solves is that an AI-prepared business case can look complete while still being unsafe to act on. CaseProof keeps the strongest outcome at ALLOW_HUMAN_REVIEW_ONLY and blocks automatic refund, record-change, claim-settlement, or case-close actions.

## What It Does

CaseProof AI checks whether an AI-prepared refund exception case is ready for a person. It looks for missing evidence, missing case milestones, policy bypasses, unsafe auto-action, and public-safety redaction gaps.

CaseProof does not issue refunds, settle claims, change customer records, close cases, or certify production readiness. Its strongest action is:

```text
ALLOW_HUMAN_REVIEW_ONLY
```

## UiPath AgentHack Alignment

- Hackathon: UiPath AgentHack 2026
- Track: UiPath Maestro Case
- Project name: CaseProof AI
- Agent type: case-governance validator for AI-prepared refund exception work
- UiPath components: UiPath Automation Cloud, UiPath Maestro, Studio Web/API Workflow handoff, optional Apps/Action Center style human review

The public repository contains a runnable clean-room prototype and synthetic demo packets. Real customer data, real tenant reports, private verifier internals, thresholds, seeds, and ranking weights are intentionally not included.

## UiPath Components Used

- UiPath Automation Cloud
- UiPath Maestro case model
- UiPath Studio Web or API Workflow handoff pattern
- Optional UiPath Apps / Action Center-style human review
- Coded Python validator
- Synthetic public-safe Maestro case packets
- Human case-review boundary

## Agent Type

CaseProof uses both a coded-agent validator and a low-code Maestro/API workflow integration path. The public repo implements the coded validator and synthetic case packet flow. The UiPath tenant binding is represented by the Maestro handoff model and review-boundary documentation.

## Why It Matters

Enterprise agents can collect refund evidence, prepare a recommendation, and route a case. But a prepared case is not an approved case. It can still be missing a customer statement, skip policy review, reuse evidence from the wrong case, or route a high-value refund too early. CaseProof adds a small gate before the case is treated as review-ready.

CaseProof checks:

- required evidence completeness
- case subject binding
- policy and amount caps
- mandatory human review routing
- required milestone presence
- unsafe auto-action disablement
- public-safe redaction status

## Setup Instructions for Judges

1. Use Python 3.10 or newer.
2. Clone the repository.
3. Optional: create and activate a virtual environment.
4. Install reviewer dependencies with `python -m pip install -r requirements-dev.txt` if needed.
5. Run the validator examples in the Quick Start section.
6. Run tests with `python -m pytest`.
7. Run the public safety scan with `python scripts/secret_scan.py .`.
8. Open `demo/index.html` to view the dashboard.
9. Run `python scripts/generate_demo_assets.py` if you want to regenerate local demo assets.
10. Review `docs/CaseProof_AI_AgentHack_Required_Template_Deck.pptx` as the required-template presentation deck.

## Quick Start

Use Python 3.10 or newer.

```bash
python -m caseproof.cli fixtures/hold_missing_evidence.json
python -m caseproof.cli fixtures/allow_review_refund_case.json
python -m caseproof.cli fixtures/block_policy_bypass.json
python -m caseproof.cli fixtures/block_stage_skip.json
```

Expected decisions:

```text
hold_missing_evidence.json       -> HOLD
allow_review_refund_case.json    -> ALLOW_HUMAN_REVIEW_ONLY
block_policy_bypass.json         -> BLOCK
block_stage_skip.json            -> BLOCK
```

Run tests:

```bash
python -m pytest
```

Run public safety scan:

```bash
python scripts/secret_scan.py .
```

Generate local demo assets:

```bash
python scripts/generate_demo_assets.py
python scripts/build_deck.py
python scripts/final_pre_submit_check.py
```

Build a review ZIP:

```bash
python scripts/build_review_package.py
```

## Demo Dashboard

Open the local dashboard:

```text
demo/index.html
```

Devpost screenshot candidate:

```text
docs/assets/caseproof_dashboard_desktop.png
```

Presentation deck draft:

```text
docs/CaseProof_AI_AgentHack_Deck_Draft.pptx
```

Required UiPath AgentHack template deck:

```text
docs/CaseProof_AI_AgentHack_Required_Template_Deck.pptx
```

## Claim Ceiling

This is a public-safe hackathon prototype over synthetic high-value refund exception packets. It is not production approval, legal compliance certification, financial authorization, security certification, or field validation. A real UiPath Maestro tenant run must bind a real case URL, process instance, evidence references, and human-review action before any product or field claim is made.

## Repository Safety Boundary

This public repository may include:

- synthetic fixtures
- bounded validators
- demo dashboard
- local tests
- public-safe docs

This public repository must not include:

- real customer data
- credentials or tenant secrets
- private negative-control banks
- hidden thresholds or ranking weights
- private verifier internals
- production approval keys
