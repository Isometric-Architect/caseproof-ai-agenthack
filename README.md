# CaseProof AI

Human-review governor for high-value refund exception cases in UiPath Maestro.

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
