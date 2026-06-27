# UiPath Components

CaseProof AI targets the UiPath Maestro Case track.

Intended flow:

1. UiPath Maestro orchestrates the case.
2. Agent steps collect evidence and prepare a recommendation.
3. Studio Web or API Workflow calls the CaseProof validator.
4. CaseProof returns HOLD, BLOCK, or ALLOW_HUMAN_REVIEW_ONLY.
5. Only a human review task may be opened.

No external business action is taken by this prototype.

