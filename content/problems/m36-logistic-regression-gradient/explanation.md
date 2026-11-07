# Differentiate a Logistic Model

Differentiating the stable logistic loss with respect to a logit gives sigmoid(logit)-label. Multiplying by each feature and averaging applies the chain rule to the weight vector.

Bias shifts every logit by the same amount, so its gradient is the mean residual. This is a parameter gradient, whereas evaluating a loss alone does not identify an update direction.
