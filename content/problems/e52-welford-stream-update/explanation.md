# Update Running Mean and Variance State

Welford updates centered moments without storing historical observations. The two different mean values in the update are necessary to account for the shifting center.

Population variance is m2/count and sample variance is m2/(count-1) when defined. Keeping m2 in the state postpones that normalization choice.

Concept references (original code and prose):

- [Welford, Note on a Method for Calculating Corrected Sums of Squares and Products](https://www.tandfonline.com/doi/abs/10.1080/00401706.1962.10490022) — Streaming count, mean, and unnormalized centered sum of squares.
