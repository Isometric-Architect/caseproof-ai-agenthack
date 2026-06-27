# Studio Web Workflow Recipe

Minimal workflow:

1. Trigger on a refund exception case reaching review preparation.
2. Build a redacted CaseProof packet from case, order, delivery, policy, and agent rationale fields.
3. Call the validator.
4. Branch on the decision.
5. HOLD asks for missing evidence.
6. BLOCK closes unsafe routing.
7. ALLOW_HUMAN_REVIEW_ONLY opens a review task.

Do not add an auto-approval branch.
Do not issue a refund from this workflow.
