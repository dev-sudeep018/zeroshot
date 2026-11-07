# Turn Uniform Draws into a Categorical Choice

Independent uniform draws transformed as -log(-log(U)) have a standard Gumbel distribution. Adding them to logits yields a sample with probabilities proportional to exponentiated logits.

With fixed supplied draws this function is deterministic. It exposes the sampling mechanism; a single outcome does not estimate a category probability.

Conceptual reading: https://arxiv.org/abs/1611.01144
