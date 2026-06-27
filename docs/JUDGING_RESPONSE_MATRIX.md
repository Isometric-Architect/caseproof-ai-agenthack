# Judging Response Matrix

## What problem does it solve?

It keeps agent-handled cases from moving to approval when evidence, policy, or process history is incomplete.

## How does it use UiPath?

UiPath Maestro is the case orchestration layer. CaseProof is the review gate inside that flow.

## What is the agentic part?

Agents prepare the case and recommendation. CaseProof checks whether that work is review-ready.

## What is the safeguard?

External action is disabled. The highest allowed result is human review.

## What is not claimed?

Production approval, legal compliance, security certification, and field validation are not claimed.

