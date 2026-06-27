# Final Devpost Fields

## Project name

CaseProof AI

## Elevator pitch

A UiPath Maestro case gate that checks evidence, policy, and stage order before an AI-handled case reaches human review.

## What are you hoping to get out of this hackathon?

I want to test a practical governance pattern for agent-handled enterprise cases in UiPath Maestro.

## About the project

```markdown
## Inspiration
AI agents can prepare business cases, but a case can look complete while evidence is missing, policy was skipped, or a risky decision was routed too quickly. CaseProof AI was built to keep that work reviewable.

## What it does
CaseProof AI checks an AI-handled UiPath Maestro case before it reaches human review. It verifies evidence, case identity, policy caps, required stages, and review routing. It returns HOLD, BLOCK, or ALLOW_HUMAN_REVIEW_ONLY.

## How we built it
The prototype uses synthetic Maestro case packets, a small Python validator, local receipts, tests, a demo dashboard, and a submission audit. The validator never approves a case. It can only open the path to human review.

## Challenges we ran into
The main challenge was drawing a clean line between useful agent work and unsafe action. A case can be well prepared, but still not safe to approve. CaseProof keeps that distinction explicit.

## Accomplishments that we're proud of
We built a public-safe prototype that catches missing evidence, policy bypasses, skipped case stages, and unsafe external action. It also keeps the claim boundary clear.

## What we learned
Agentic case work needs a small proof step before approval. The useful question is not only "what did the agent decide?" but "what evidence and process path support that decision?"

## What's next for CaseProof AI
Next we would bind this packet shape to a real UiPath Maestro case, a Studio Web or API Workflow call, and a human review task.
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
CaseProof AI dashboard showing HOLD, human-review-only, and BLOCK outcomes for UiPath Maestro case packets.
```

