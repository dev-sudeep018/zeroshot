# Evaluate Binomial Evidence in Log Space

The binomial coefficient counts which trial positions could contain the observed successes. Omitting it computes one particular sequence probability rather than the probability of the count.

Zero observations contribute no evidence. Endpoint probabilities need explicit handling so that a zero count times log(0) does not produce an undefined intermediate value.
