# Aggregate a Grid into Partial Blocks

The output grid summarizes disjoint spatial regions. Ceiling division is necessary because a partial region still contains observations and must appear in the result.

A useful conservation check is that the sum of all output blocks equals the sum of the original grid. This catches both dropped edges and accidentally overlapping blocks.
