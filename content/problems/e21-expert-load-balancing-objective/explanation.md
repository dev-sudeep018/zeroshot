# Inspect Expert Loads and Router Probabilities

Balanced hard loads give loss one, but a value of one does not certify balanced routing. Uniform tied probabilities also give one while the hard assignments may all select the first expert.

Confident collapse can drive the loss toward E. One is not a universal mathematical lower bound for this finite-batch statistic, so inspect the two returned distributions instead of treating the scalar as a balance certificate.

Ported the upstream top-one load-balancing statistic to NumPy with stable softmax and deterministic index-order ties. Exposed the hard fractions and mean probabilities for direct inspection.

Adapted code source: https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/torch_judge/tasks/moe_load_balance.py
