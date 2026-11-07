# Differentiate the Margin Penalty

The hinge penalty is linear when the signed score is below one and flat above one. Its active set therefore depends on the margin, not just the predicted class.

The derivative is not unique exactly at the kink. Choosing zero there gives a deterministic contract; averaging by all observations keeps the loss and gradient scales consistent.
