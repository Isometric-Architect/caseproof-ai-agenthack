# Maestro Case Blueprint

This is the intended UiPath shape.

1. Maestro opens or updates a case.
2. Agent steps collect evidence.
3. The case reaches policy check.
4. CaseProof validates the packet.
5. If HOLD, the case asks for more evidence.
6. If BLOCK, the case stops unsafe action.
7. If ALLOW_HUMAN_REVIEW_ONLY, a person reviews it.

The prototype uses synthetic packets. A real tenant run should bind a real case URL and process instance.

