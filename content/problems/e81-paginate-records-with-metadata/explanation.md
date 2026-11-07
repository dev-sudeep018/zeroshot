# Paginate Records with Metadata

Pagination returns both a subset and enough metadata to navigate the rest. A caller should not have to infer whether another page exists from a full-looking final page.

This contract operates on a fixed in-memory snapshot. Real mutable datasets may need cursor semantics, but offset boundaries are useful to understand before adding that complexity.
