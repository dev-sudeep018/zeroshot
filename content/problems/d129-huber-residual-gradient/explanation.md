# Limit Outlier Influence with Huber Loss

The quadratic region is sensitive to small errors, while the linear tails limit the effect of large residuals on the gradient. Delta controls where that transition happens.

The derivative of the mean differs from the per-item derivative by the number of items. This scaling matters when connecting a loss implementation to a batch optimizer.
