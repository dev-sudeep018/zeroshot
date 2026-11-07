# Construct Split-Conformal Intervals

Split conformal uses heldout residuals to choose an error threshold. The corrected rank is more conservative than an ordinary sample percentile and matters most for small samples.

Coverage interpretation requires exchangeability between calibration and future examples. The code constructs intervals but does not assert that the assumption holds in a deployed system.

Concept references (original code and prose):

- [Angelopoulos and Bates, A Gentle Introduction to Conformal Prediction](https://arxiv.org/abs/2107.07511) — Absolute-residual split-conformal intervals and descriptive coverage; finite rank required and exchangeability assumption stated.
