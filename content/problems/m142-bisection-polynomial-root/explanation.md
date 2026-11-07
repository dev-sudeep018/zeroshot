# Keep a Root inside a Shrinking Bracket

Bisection trades speed for a strong geometric guarantee: a continuous function with opposite endpoint signs has a root inside the bracket. Every ordinary iteration halves that bracket.

The midpoint is an estimate with error bounded by half the bracket width. Compare signs directly: multiplying tiny endpoint values can underflow and lose their sign relationship. Exact floating-point zero is handled separately from the fixed iteration budget.
