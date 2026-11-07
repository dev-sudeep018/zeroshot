# Filter Stopwords Without Reordering

Stopword filtering removes a supplied vocabulary from tokenized text. Retaining repetition matters because later frequency-based features still need the number of surviving occurrences.

The policy is explicit rather than language-dependent. Case folding or punctuation stripping must happen in a separate stage if a pipeline wants those behaviors.
