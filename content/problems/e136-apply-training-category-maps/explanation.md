# Apply Training Category Maps

Feature preprocessing should learn its vocabulary from training data only. Holding that mapping fixed gives an honest picture of unseen categories during evaluation.

First-occurrence IDs make the fit deterministic for a fixed training order. Unknown heldout values use a reserved negative code and remain visible through their positions.
