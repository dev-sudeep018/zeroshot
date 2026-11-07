# Decode the Strongest Heatmap Location

Peak decoding selects a location that actually attains the largest supplied score. It can differ substantially from the center of mass when the map contains multiple modes.

Deterministic row-major tie handling makes equal-score results reproducible. The returned score need not be a probability because this contract accepts any finite response values.
