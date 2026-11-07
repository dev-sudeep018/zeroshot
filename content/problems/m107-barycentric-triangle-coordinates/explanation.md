# Locate a Point Relative to a Triangle

Barycentric coordinates describe a point as an affine combination of a triangle vertices. They are useful for interpolating values attached to vertices because the same coefficients apply to those values.

A point inside or on the triangle is a convex combination, so its coefficients are nonnegative. Outside points require at least one negative coefficient, while a degenerate triangle cannot supply a unique coordinate system.
