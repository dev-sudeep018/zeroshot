# Detect Conflicting Task Gradients

A negative dot product means a step improving one linearized task can worsen the other. Cosine similarity removes magnitude to isolate this directional disagreement.

The audit is local to the supplied gradients. It does not modify them or establish long-term task incompatibility, and zero gradients have no defined direction under the chosen zero convention.

Orthogonal directions can produce a tiny signed residual because floating-point reductions differ across runtimes. The explicit 1e-12 zero band prevents that residual from becoming a conflict. Scale each nonzero row before taking its norm so extremely small gradients retain their direction.
