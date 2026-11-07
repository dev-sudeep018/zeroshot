# Parse URL Query Pairs

Query parameters can repeat, so parsing into a single value per key loses information. A multimap preserves repeated filters and their order.

Decoding happens after structural splitting because an encoded ampersand belongs inside a value. Strict percent and UTF-8 validation avoids silently replacing malformed data.
