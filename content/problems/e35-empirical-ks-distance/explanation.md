# Compare Empirical Distributions with KS Distance

The empirical CDF is a step function, so a maximum gap occurs on the pooled support. Right-sided counts handle ties as one jump rather than arbitrarily ordering equal observations.

This lesson computes a descriptive distance only. Statistical significance requires additional assumptions and a p-value procedure; those are deliberately separate from the distance.

Concept references (original code and prose):

- [SciPy two-sample Kolmogorov-Smirnov documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ks_2samp.html) — Descriptive two-sided empirical-CDF distance only; deterministic earliest maximizer and no p-value.
