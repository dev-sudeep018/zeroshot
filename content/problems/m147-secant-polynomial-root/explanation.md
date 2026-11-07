# Update a Root Estimate from Two Function Values

The secant method estimates a derivative from two function values, so it can approach a root without an analytic derivative. Unlike bisection it does not retain a guaranteed bracket.

Flat secants and escaping estimates need explicit policies. The bounded contract makes such failures visible instead of returning a misleading large or nonfinite value.
