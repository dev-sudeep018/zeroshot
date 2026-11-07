# Compute Retrieval Precision at a Cutoff

Precision at a cutoff evaluates the usefulness of a fixed number of displayed result slots. Repeating the same relevant item should not earn repeated credit.

Taking unique IDs before truncation would let duplicates disappear and pull later results into the evaluated window. The order of cutoff and deduplication therefore changes the metric.
