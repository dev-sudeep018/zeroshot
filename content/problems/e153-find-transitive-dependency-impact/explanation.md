# Find Transitive Dependency Impact

Change impact finds downstream consumers that may need review after an input changes. It follows the direction in which data or build results flow.

Unlike execution ordering, impact reachability can be computed on a cyclic graph. Excluding every seed keeps the report focused on additional affected components.
