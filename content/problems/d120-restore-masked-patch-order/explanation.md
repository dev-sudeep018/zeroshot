# Restore Visible Patches to Their Original Positions

Restoring order makes the decoder’s positional layout match the original image grid. The visible rows arrive in encoder order, so the position mapping must be applied to each corresponding embedding.

A mask token is an embedding rather than a literal zero. Returning the mask separately keeps missingness observable even when a visible embedding happens to equal the token.
