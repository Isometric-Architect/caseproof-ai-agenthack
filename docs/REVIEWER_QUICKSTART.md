# Reviewer Quickstart

Run the four demo packets:

```bash
python -m caseproof.cli fixtures/hold_missing_evidence.json --pretty
python -m caseproof.cli fixtures/allow_review_refund_case.json --pretty
python -m caseproof.cli fixtures/block_policy_bypass.json --pretty
python -m caseproof.cli fixtures/block_stage_skip.json --pretty
```

Run tests:

```bash
python -m pytest
```

Open:

```text
demo/index.html
```

Expected decisions:

```text
HOLD
ALLOW_HUMAN_REVIEW_ONLY
BLOCK
BLOCK
```

