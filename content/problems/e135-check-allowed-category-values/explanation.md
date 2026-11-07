# Check Allowed Category Values

Category validation protects a fixed vocabulary from unexpected labels or inconsistent types. It reports all offending rows so ingestion can produce a complete quality report.

Coercing numeric cells to strings would hide an input-type error. Explicitly allowing an empty string is possible, but it must appear in the supplied vocabulary.
