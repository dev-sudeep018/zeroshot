# Compare Paired Outcomes with an Exact Sign Test

The exact sign test discards effect magnitudes and uses only the direction of nonzero paired changes. It avoids treating the two systems as independent samples.

A small p-value is evidence against the fair-sign null, not a measurement of practical benefit. Report the paired effect sizes alongside this sign-based diagnostic when interpreting real results.

Concept references (original code and prose):

- [SciPy exact binomial test documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html) — Fair-sign null with ties excluded; exact doubled smaller tail for p=0.5.
