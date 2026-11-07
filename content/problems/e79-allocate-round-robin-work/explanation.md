# Allocate Round-Robin Work

Round-robin scheduling spreads the number of jobs evenly without considering job duration. Worker queue sizes differ by at most one because assignments cycle through workers.

Independent worker lists are essential: constructing several references to the same list creates aliasing. This lesson exposes that common Python container mistake in a practical setting.
