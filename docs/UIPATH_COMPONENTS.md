# UiPath Components

CaseProof AI targets the UiPath Maestro Case track through a high-value refund exception scenario.

Intended flow:

1. UiPath Maestro opens a refund exception case.
2. An agent reads the request and prepares a recommendation.
3. RPA or API steps fetch order, delivery, and policy evidence.
4. Studio Web or API Workflow calls the CaseProof validator.
5. CaseProof returns HOLD, BLOCK, or ALLOW_HUMAN_REVIEW_ONLY.
6. Only a human review task may be opened.

No external business action is taken by this prototype.

CaseProof does not issue refunds, settle claims, update customer records, or close cases.
