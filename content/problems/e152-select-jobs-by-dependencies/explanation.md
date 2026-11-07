# Select Jobs by Dependencies

Dependency ordering turns a graph of prerequisites into an executable task sequence. Shared prerequisites should run once before every dependent task.

Stable choice among currently ready tasks makes builds reproducible. A pass with no ready task while work remains reveals a cycle rather than a reason to emit an arbitrary task.
