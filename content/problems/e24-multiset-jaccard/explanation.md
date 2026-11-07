# Compare Repeated Terms with Multiset Jaccard

Multiset Jaccard retains token multiplicity, unlike ordinary set Jaccard. Repeating one token can lower similarity even when both documents have the same vocabulary.

The score is symmetric and lies in [0,1]. It ignores word order; n-gram multisets can introduce local order when that distinction matters.
