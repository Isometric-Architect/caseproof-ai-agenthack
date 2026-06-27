# One Page Reviewer Summary

CaseProof AI is a small gate for high-value refund exception cases in UiPath Maestro.

An agent may prepare a refund case and recommend an action. CaseProof checks whether the packet is complete enough for a person to review.

It checks:

- evidence
- case identity
- policy caps
- required Maestro milestones
- review route
- external action status

It returns:

- HOLD
- BLOCK
- ALLOW_HUMAN_REVIEW_ONLY

It never approves a case.
