# Solve a Small System with Partial Pivoting

Elimination turns a coupled linear system into an upper-triangular one. Partial pivoting avoids dividing by a needlessly small entry when a larger one is available below it.

The target vector is part of each equation, so every row operation must affect it too. A residual against the original unmodified system verifies the result independently.
