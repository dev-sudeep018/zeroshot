# Find Peaks without Double-Counting Plateaus

Comparing each cell independently would either miss flat peaks or count the same peak repeatedly. Grouping equal runs makes the peak decision about the whole plateau.

Endpoint exclusion is a deliberate convention: without observations on both sides, the exercise cannot establish a local rise and fall. Midpoint rounding is fixed so even plateaus have deterministic locations.
