# Sample a Stream with a Fixed-Size Reservoir

At arrival i, an independent uniform draw from 0 through i admits the new item with probability capacity/(i+1). Induction then gives every observed item equal inclusion probability.

Supplying the draws separates deterministic state transitions from random-number generation. The returned reservoir is in slot order and does not imply a random ordering of the selected items.

Concept references (original code and prose):

- [Vitter, Random Sampling with a Reservoir](https://www.cs.usfca.edu/~mmalensek/cs677/schedule/papers/vitter1985random.pdf) — Basic reservoir replacement with supplied integer draws; not Algorithm Z or a random-number generator.
