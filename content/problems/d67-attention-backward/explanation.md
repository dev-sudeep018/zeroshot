# Trace Gradients through Attention Scores and Values

A single-key attention output cannot depend on query or key scores, so their gradients vanish while the value still receives upstream.

The scale factor belongs to both query and key derivatives. Finite differences against the complete attention objective can detect missing transpose or normalization terms.
