# Count Adjacent Status Transitions

Transition counts summarize how a process moves between states. They retain direction, so open-to-closed and closed-to-open are separate events.

This is not run-length compression: self transitions are counted rather than collapsed. For a nonempty trace, the sum of all counts must equal the trace length minus one.
