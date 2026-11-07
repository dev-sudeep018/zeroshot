# Apply Sequential Balance Changes

A state transition can be accepted or rejected without changing the number of events in a trace. Keeping both the balance and an acceptance flag makes rejected operations visible.

The invariant is nonnegative balance after every attempt. Rejecting an overdraft must preserve the previous balance rather than clipping it to zero or allowing a later deposit to hide the error.
