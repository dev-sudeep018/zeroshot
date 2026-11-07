# Share Key and Value Heads across Query Groups

Different queries sharing the same keys can still produce different mixtures. Sharing a value head does not force the outputs of its query group to be identical.

The NumPy port makes the upstream repeat-interleave head mapping explicit, without allocating repeated key/value arrays.
