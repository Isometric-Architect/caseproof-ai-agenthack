# Maestro Case Flow

Scenario: high-value refund exception.

```mermaid
flowchart LR
  A["Intake: refund request"] --> B["Evidence collection: order, delivery, customer statement"]
  B --> C["Policy check: refund rules and amount cap"]
  C --> D["Risk review: high-value exception"]
  D --> E["CaseProof gate"]
  E -->|HOLD| F["Ask for missing evidence"]
  E -->|BLOCK| G["Stop unsafe routing"]
  E -->|ALLOW_HUMAN_REVIEW_ONLY| H["Open human review task"]
```

CaseProof is not the approval step.

It only asks whether the case packet is complete enough for a person to review.

It does not issue a refund, settle a claim, update a customer record, or close a case.

