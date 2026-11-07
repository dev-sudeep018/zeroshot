# Intersect and Exclude Posting Lists

Boolean retrieval is independent of ranking: a document either satisfies every condition or it does not. Set intersection expresses all required terms, while set difference handles exclusions.

Missing required terms must produce no results. Treating them as absent query constraints would silently broaden the query and return incorrect documents.
