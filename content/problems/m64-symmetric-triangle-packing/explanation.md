# Pack a Symmetric Measurement Matrix

A symmetric matrix contains redundant mirrored entries. Fixed upper-triangle traversal preserves the independent values while making serialization order deterministic.

Validation should happen before packing, since otherwise an asymmetric matrix would silently lose information. The reconstruction uses exactly the chosen upper values rather than averaging conflicting observations.
