# One Page Reviewer Summary

CaseProof AI is a small gate for AI-handled UiPath Maestro cases.

An agent may prepare a case and recommend an action. CaseProof checks whether the packet is complete enough for a person to review.

It checks:

- evidence
- case identity
- policy caps
- Maestro stage order
- review route
- external action status

It returns:

- HOLD
- BLOCK
- ALLOW_HUMAN_REVIEW_ONLY

It never approves a case.

