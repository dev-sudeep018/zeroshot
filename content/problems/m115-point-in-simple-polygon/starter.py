import numpy as np


def points_in_polygon(points, vertices):
    """Use horizontal ray crossings to test membership in a simple polygon, treating boundary points as inside."""
    # First: Check whether a query lies on any edge before counting ray intersections.
    # Then: Toggle membership only for edges whose endpoint heights straddle the query using one strict and one inclusive side.
    raise NotImplementedError("Complete the calculation and input checks")
