# Maestro Case Blueprint

This is the intended UiPath shape for a high-value refund exception case.

1. Maestro opens or updates the refund exception case.
2. Agent steps read the request and prepare a recommendation.
3. RPA or API steps fetch order, delivery, and policy evidence.
4. CaseProof validates the packet through Studio Web or API Workflow.
5. If HOLD, the case asks for missing evidence.
6. If BLOCK, the case stops unsafe routing.
7. If ALLOW_HUMAN_REVIEW_ONLY, a person reviews the packet.

The prototype uses synthetic packets. A real tenant run should bind a real case URL and process instance.
