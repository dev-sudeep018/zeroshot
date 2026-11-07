# Canonicalize JSON for Cache Keys

Cache keys need consistent representation when dictionary insertion order differs. Sorting object keys and fixing separators removes those incidental formatting differences.

Arrays keep their order because order is part of their meaning. This deterministic Python encoding is useful within a controlled pipeline without claiming every runtime encodes numbers identically.
