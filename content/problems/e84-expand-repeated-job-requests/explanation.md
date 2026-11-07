# Expand Repeated Job Requests

Compact job requests separate a task identity from how many copies should run. Expansion materializes the execution order and makes repetitions explicit.

A bound on input length alone does not bound expanded output. Checking the cumulative count prevents a small request list from allocating an unexpectedly large queue.
