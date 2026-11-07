# Identify Density-Based Core Points

The neighbor matrix represents local density using an inclusive distance threshold. Counting the diagonal follows the convention that an observation belongs to its own neighborhood.

Core membership is only one stage of density clustering. Border and noise classification also require connectivity through core points and should not be inferred from this boolean vector alone.
