# Count Monotone Routes around Blocked Cells

Monotone movement creates an acyclic dependency structure. Every path reaching a cell must arrive from exactly one of two preceding neighbors, so their path counts add.

Boundary initialization matters: the start contributes one empty path only when it is open. Exact Python integers retain large combinatorial counts that fixed-width integer arrays could overflow.
