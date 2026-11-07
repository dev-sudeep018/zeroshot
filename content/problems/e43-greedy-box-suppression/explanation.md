# Suppress Redundant Detection Boxes

Greedy NMS is order-dependent: a high-confidence box is retained first and can suppress lower-ranked alternatives. The algorithm does not optimize a global set objective.

Only overlaps strictly above the threshold are suppressed. That boundary and the tie policy make deterministic evaluation possible across implementations.
