# Presentation Deck Draft

## Slide 1

CaseProof AI

A human-review gate for high-value refund exception cases in UiPath Maestro.

## Slide 2

Problem

An agent can prepare a refund case that looks complete while evidence, policy, or review routing is wrong.

## Slide 3

Validator

CaseProof checks evidence, case identity, required Maestro milestones, policy caps, and review route.

## Slide 4

Outcomes

HOLD means not enough evidence.

BLOCK means unsafe or invalid.

ALLOW_HUMAN_REVIEW_ONLY means the case may go to a person.

## Slide 5

UiPath fit

Maestro remains the orchestration layer. The validator is a small gate in the case flow.

## Slide 6

Boundary

Synthetic demo only. No production approval or compliance claim.
