# Gather the Final Real Sequence State

Length-aware selection prevents padded states from replacing meaningful sequence summaries. It also supports a batch where some examples are empty without inventing a last token.

The gathered state is whatever representation the model supplied at that position. Whether it summarizes the whole prefix depends on the network architecture, not on this indexing operation.
