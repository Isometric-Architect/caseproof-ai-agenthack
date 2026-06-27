# Contributing

This repository is intentionally small and public-safe for UiPath AgentHack review.

Contributions should preserve:

- synthetic or redacted data only
- no credentials
- no real customer data
- no private verifier internals
- no auto-approval or external action claims
- explicit claim ceilings

Run before submitting changes:

```bash
python -m pytest
python scripts/secret_scan.py .
python scripts/final_pre_submit_check.py
```

