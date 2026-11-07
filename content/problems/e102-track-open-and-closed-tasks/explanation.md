# Track Open and Closed Tasks

A small state machine distinguishes syntactically valid events from valid transitions. Reporting a duplicate open rather than raising lets the audit continue through the rest of a trace.

Invalid transitions must not alter state. The resulting open set therefore reflects only accepted lifecycle events, while their original positions remain available for debugging.
