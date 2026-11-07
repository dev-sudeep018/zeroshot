# Plan a Minimal Incremental Rebuild

Incremental builds avoid repeating work whose inputs and dependencies are unchanged. Fingerprint changes seed a dirty set that propagates through the dependency graph.

The returned order is executable because prerequisites appear first. This model assumes fingerprints describe all local inputs; omitted dependencies can make any incremental planner reuse stale results.
