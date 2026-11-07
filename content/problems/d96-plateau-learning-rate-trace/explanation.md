# Reduce Learning Rate on a Validation Plateau

Reducing the step size can permit finer updates near a plateau. The explicit floor prevents repeated reductions from making the rate arbitrarily small.

A reduction does not erase the best validation observation. Keeping that reference avoids treating unchanged performance as an improvement merely because the optimizer rate changed.
