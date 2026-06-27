# Demo Video Script

## 0:00

CaseProof AI is a human-review gate for UiPath Maestro cases.

## 0:20

The problem is simple. An agent can prepare a case, but the case may still be unsafe to approve.

## 0:45

CaseProof reads a public-safe case packet. It checks evidence, policy, stage order, and review routing.

## 1:20

First case: evidence is missing. CaseProof returns HOLD.

## 1:55

Second case: the packet is complete. CaseProof allows human review only.

## 2:30

Third case: the agent tries to bypass policy and auto-approve a high-value refund. CaseProof blocks it.

## 3:05

Fourth case: required Maestro stages were skipped. CaseProof blocks it.

## 3:40

The boundary is important. CaseProof does not approve a case. It only helps decide whether a person can review it.

