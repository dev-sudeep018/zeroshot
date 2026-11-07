# Apply a Versioned Cache Policy

A cache may contain structurally valid values produced by an obsolete computation version. Version and age checks jointly determine whether a value can be reused.

Future timestamps are excluded instead of receiving extra lifetime. Copying accepted values prevents a caller from accidentally mutating the cache through the returned mapping.
