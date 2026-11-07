# Step through a First-Order Cooling Model

Explicit Euler converts a differential cooling rule into small discrete updates. The time-step size changes the numerical trajectory even when the underlying rate is fixed.

With the documented coefficient bound each update is a convex combination of the current temperature and ambient. This guarantees monotone relaxation without overshoot for these exercises.
