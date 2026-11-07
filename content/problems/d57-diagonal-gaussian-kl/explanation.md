# Measure a Latent Gaussian against a Unit Prior

The location term penalizes squared distance from the prior mean. The uncertainty term is minimized at unit variance and grows for both very narrow and very broad distributions.

Summing coordinates gives one divergence per example. A separate training objective may later average these values or apply a coefficient.
