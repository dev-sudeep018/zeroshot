# Audit Sigmoid Saturation

The derivative measures a probability’s response to a small logit change. It approaches zero when probabilities approach either endpoint, which can slow gradient transmission.

Saturation is defined here by a chosen diagnostic threshold. Its batch frequency distinguishes consistently saturated units from occasional confident responses.
