# Sessionize Events by Inactivity

Session boundaries depend on inactivity between neighboring events. A long session can continue indefinitely while each next event arrives within the timeout.

Returning indices preserves a link to original records even when timestamps repeat. Sorting is required from the caller so the function does not silently reorder observations.
