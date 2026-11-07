# Normalize and Deduplicate Tags

Imported tags often differ only in surrounding whitespace or letter case. Cleaning before deduplication lets equivalent labels share one identity while preserving the first-seen ordering.

A set alone loses the output sequence. Keep a result list for order and optionally a separate set for membership; normalization is deliberately lower(), not Unicode casefold().
