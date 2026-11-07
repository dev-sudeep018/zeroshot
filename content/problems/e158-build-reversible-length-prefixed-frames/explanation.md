# Build Reversible Length-Prefixed Frames

Length-prefixed frames can carry text containing any delimiter without escaping it. The length counts bytes so a decoder can locate the next frame before interpreting text.

Strict length syntax removes alternate encodings of the same frame. Truncation and invalid UTF-8 must be reported rather than returning a partial decoded result.
