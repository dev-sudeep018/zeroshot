# Find the Nearest Point on a Segment

A line projection may land outside a finite segment. The closest point then moves to the nearest endpoint, which is exactly what clamping the parameter accomplishes.

The returned parameter also describes how far along the segment the match occurs. A degenerate segment has no direction, so its only possible nearest point is the shared endpoint.
