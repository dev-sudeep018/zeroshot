# Train for an Asymmetric Quantile

Underestimation and overestimation have different slopes. At a high quantile, an underestimate is penalized more strongly, shifting a fitted constant toward the upper part of the observations.

The reported vector differentiates the mean loss, so each component includes division by the observation count. At zero residual the loss has a kink and this exercise chooses the zero subgradient.
