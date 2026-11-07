# Clip a Segment to a Rectangle

Clipping turns spatial constraints into restrictions on one parameter along the segment. The final visible portion is the intersection of all those restrictions.

Closed bounds preserve tangent or corner contacts as a zero-length visible portion. The explicit empty-result convention makes a missed rectangle distinguishable from a genuine point at the origin.
