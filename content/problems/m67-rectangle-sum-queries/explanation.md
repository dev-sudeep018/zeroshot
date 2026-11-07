# Answer Rectangular Sum Queries

A prefix table stores the sum from the origin to each boundary. Inclusion and exclusion of its four corners removes the unwanted strips while restoring the strip intersection.

Half-open rectangles compose cleanly: adjacent regions share a boundary but never share a cell. The same formula also handles empty rectangles without a special numerical case.
