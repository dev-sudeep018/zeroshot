# Index Unique Records

An ID index replaces repeated linear searches with direct dictionary lookups. Keeping the complete record as the value preserves every field for downstream processing.

Duplicate identifiers make the lookup ambiguous. Detecting them during index construction prevents a later record from silently replacing an earlier one.
