# Classify Points against a Polygon Boundary

A ray starting inside a simple polygon crosses its boundary an odd number of times before reaching infinity. Outside points have an even crossing count.

Vertices and horizontal edges need careful handling to prevent duplicate crossings. Separating the boundary test from the half-open crossing rule makes edge and corner membership explicit, including for concave polygons.
