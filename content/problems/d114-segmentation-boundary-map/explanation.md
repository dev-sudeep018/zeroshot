# Mark Boundaries between Segmentation Regions

A boundary map converts a region labeling into local transitions. Marking both sides avoids selecting an arbitrary foreground class and works for multiple semantic classes.

The neighborhood and outside-image convention are part of the definition. Diagonal-only contact does not count here, and the image border becomes a boundary only when an actual in-bounds neighbor differs.
