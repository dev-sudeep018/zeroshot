# Merge Configuration Layers

Layered settings support defaults, environment overrides, and later corrections. A precise deletion rule lets a later layer remove a setting rather than merely mask it.

Replacing nested values atomically keeps the policy simple and predictable. Recursive merges use different semantics and would incorrectly retain nested keys in this lesson.
