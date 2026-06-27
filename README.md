# CaseProof AI

Human-review governor for AI-handled enterprise cases in UiPath Maestro.

## What It Does

CaseProof AI checks whether an AI-handled business case is safe to send to human approval. It looks for missing evidence, skipped process stages, policy bypasses, unsafe auto-action, and public-safety redaction gaps.

CaseProof does not approve refunds, settle claims, change customer records, or certify production readiness. Its strongest action is:

```text
ALLOW_HUMAN_REVIEW_ONLY
```

## UiPath AgentHack Alignment

- Hackathon: UiPath AgentHack 2026
- Track: UiPath Maestro Case
- Project name: CaseProof AI
- Agent type: case-governance validator for agent-handled work
- UiPath components: UiPath Automation Cloud, UiPath Maestro, Studio Web/API Workflow handoff, optional Apps/Action Center style human review

The public repository contains a runnable clean-room prototype and synthetic demo packets. Real customer data, real tenant reports, private verifier internals, thresholds, seeds, and ranking weights are intentionally not included.

## Why It Matters

Enterprise agents can collect evidence, recommend decisions, and route cases. But an agentic case can look complete while it has skipped a policy check, reused evidence from the wrong case, or made a high-risk decision without approval. CaseProof adds a small governance gate before any action is treated as review-ready.

CaseProof checks:

- required evidence completeness
- case subject binding
- policy and amount caps
- mandatory human review routing
- stage-order continuity
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

This is a public-safe hackathon prototype over synthetic case packets. It is not production approval, legal compliance certification, financial authorization, security certification, or field validation. A real UiPath Maestro tenant run must bind a real case URL, process instance, evidence references, and human-review action before any product or field claim is made.

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

