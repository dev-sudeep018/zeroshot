# Describe a Point Cloud with a Bounding Box

An axis-aligned bounding box is a compact summary of the occupied coordinate ranges. It is useful for spatial indexing and clipping even though it may contain large empty regions.

The box center depends only on extreme coordinates, while a centroid depends on the distribution of all points. Repeating an interior point changes a centroid but leaves these bounds unchanged.
