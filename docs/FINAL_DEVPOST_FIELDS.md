# Final Devpost Fields

## Project name

CaseProof AI

## Elevator pitch

A UiPath Maestro case gate that checks evidence, policy, and required milestones before an AI-prepared refund case reaches human review.

## What are you hoping to get out of this hackathon?

I want to test a practical governance pattern for AI-prepared refund exception cases in UiPath Maestro.

## About the project

```markdown
## Inspiration
AI agents can prepare business cases quickly. But a prepared case is not the same as an approved case. In refund, claim, onboarding, or exception workflows, a packet may still be missing evidence, skip a policy check, or route a risky action too early.

## What it does
CaseProof AI is a review gate for AI-prepared UiPath Maestro cases. It checks whether a case packet has the required evidence, the same case identity, required milestones, policy limits, a human review route, and no enabled external business action.

It returns HOLD, BLOCK, or ALLOW_HUMAN_REVIEW_ONLY. It never approves the case.

## How we built it
We built a public-safe prototype with synthetic Maestro-shaped refund case packets, a Python validator, local receipts, tests, a demo dashboard, and a submission audit. The intended UiPath flow is: Maestro orchestrates the case, an agent prepares a recommendation, Studio Web or an API Workflow calls CaseProof, and only a human review task may be opened.

## Challenges we ran into
The hard part was keeping the boundary clear. Agents can help prepare work, but they should not silently turn preparation into approval. CaseProof keeps the approval step separate.

## Accomplishments that we're proud of
The prototype catches missing evidence, case identity mismatch, policy bypass, skipped required milestones, unsafe external action, and public-safety redaction issues. The strongest allowed result is human review only.

## What we learned
The useful question is not only "what did the agent recommend?" It is also "what evidence, policy path, and review route support that recommendation?"

## What's next for CaseProof AI
Next, we would bind the packet to a real UiPath Maestro case instance, call the validator through Studio Web or an API Workflow, and attach the receipt to a human review task.
```

## Built with

UiPath Automation Cloud, UiPath Maestro, UiPath Studio Web, Python, GitHub, Codex

## Try it out links

GitHub repo:

```text
https://github.com/Isometric-Architect/caseproof-ai-agenthack
```

Demo video:

```text
TBD
```

## Additional info

Begin date:

```text
27/06/2026
```

Track:

```text
UiPath Maestro Case
```

Region:

```text
APAC (Asia-Pacific)
```

Individual or team:

```text
Individual
```

UiPath Labs/environment URL:

```text
https://cloud.uipath.com/runproofailab/portal_/home
```

GitHub public code repository:

```text
https://github.com/Isometric-Architect/caseproof-ai-agenthack
```

Presentation deck:

```text
https://github.com/Isometric-Architect/caseproof-ai-agenthack/blob/main/docs/CaseProof_AI_AgentHack_Deck_Draft.pptx
```

How likely are you to use UiPath moving forward?

```text
Very likely, this hackathon has convinced me
```

How has building this project improved your skills/workflow/productivity?

```text
It helped me turn an agentic case workflow into a clearer evidence and review pattern. I learned how to separate useful agent preparation from unsafe automatic action.
```

## Image caption

```text
CaseProof AI dashboard showing HOLD, human-review-only, and BLOCK outcomes for high-value refund exception packets.
```
