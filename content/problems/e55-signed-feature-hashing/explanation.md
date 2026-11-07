# Map Tokens into a Fixed Feature Space

Hashing bounds feature memory independently of vocabulary size. The cost is collisions: different tokens may share a coordinate and become indistinguishable to a downstream linear model.

This lesson fixes the hash function to make every collision inspectable. Production choices can use better-distributed hashes; Python built-in hash is unsuitable for this deterministic contract because its string results may vary between processes.

Concept references (original code and prose):

- [scikit-learn FeatureHasher documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html) — Concept of signed feature hashing; the lesson uses its own explicit polynomial teaching hash, not MurmurHash or sklearn parity.
