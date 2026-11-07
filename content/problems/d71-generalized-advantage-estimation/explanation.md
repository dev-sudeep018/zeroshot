# Combine Temporal-Difference Residuals with GAE

At trace decay zero, the estimate is the one-step residual. At trace decay one, adding the current value back telescopes the residual sequence into a bootstrapped return.

Intermediate trace decay values reduce the influence of distant residuals. This is an estimator from a fixed rollout, not a guarantee of improved policy learning.

Conceptual reading: https://arxiv.org/abs/1506.02438
