# Count Overlapping Token N-grams

There are max(0, L-n+1) windows in a sequence of length L. Counting these windows produces a multiset rather than a set of phrases.

Overlaps are essential: the bigram (a,a) occurs twice in three consecutive a tokens. This representation is useful for corpus diagnostics and language-model statistics.
