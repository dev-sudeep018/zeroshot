# Smooth a Signal at Its Boundaries

A centered smoother combines evidence from both sides of a sample. It is useful for inspecting a completed signal but cannot serve as a causal forecast without future data.

Shrinking windows avoid artificial padding values. Counts reveal the smaller amount of supporting data near each edge and keep a constant signal constant everywhere.
