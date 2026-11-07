# Select Weighted Samples with Exponential Keys

Exponential-key sampling associates each item with a random race time. Taking the largest log-uniform keys is equivalent to taking the smallest negative-log-uniform times divided by weight.

The algorithm defines a particular weighted-without-replacement distribution. It should not be interpreted as independently including each item with a simple normalized probability.

Concept references (original code and prose):

- [Efraimidis, Weighted Random Sampling over Data Streams](https://arxiv.org/abs/1012.0256) — Logarithmic priority equivalent of exponential keys, supplied draws, sampling without replacement.
