# Compare Boxes with Intersection over Union

IoU normalizes intersection area by the combined area covered by either box. It is symmetric and stays in [0,1] for valid boxes.

Continuous-coordinate geometry has no pixel-inclusive +1 term. Declaring the coordinate convention prevents a subtle disagreement between otherwise similar detection implementations.
