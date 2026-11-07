# Serialize CSV Records in Schema Order

Serialization must quote separators, line breaks, and quotes consistently to remain readable by another parser. Explicit field order gives the file a stable schema.

Keeping conversion strict preserves the distinction between a missing value and an empty string. The final newline and line-ending choice are part of the output contract.
