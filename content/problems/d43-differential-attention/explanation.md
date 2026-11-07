# Subtract Two Attention Maps

Signed mixing can produce outputs outside the range of the supplied values. That is expected because the subtraction removes the convex-combination constraint.

This port takes the two query/key subspaces separately instead of splitting a projected feature tensor as the upstream implementation does.
