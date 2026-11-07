# Audit Interval Coverage and Width

Empirical coverage is the fraction of evaluated targets inside their intervals. Mean width supplies the second dimension needed to distinguish informative coverage from trivially broad intervals.

These observations do not guarantee future coverage. Dataset shift and small evaluation samples can make a seemingly well-calibrated model unreliable.

Concept references (original code and prose):

- [Angelopoulos and Bates, A Gentle Introduction to Conformal Prediction](https://arxiv.org/abs/2107.07511) — Absolute-residual split-conformal intervals and descriptive coverage; finite rank required and exchangeability assumption stated.
