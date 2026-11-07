# Normalize Relative Resource Paths

Resource paths often need lexical normalization before lookup. A stack resolves dot segments while preserving ordinary segment names and their order.

This is a lexical resource-name exercise, not a filesystem security check. It does not resolve symlinks, percent escapes, or operating-system path aliases.
