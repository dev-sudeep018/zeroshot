# Build a Positional Posting Index

A positional inverted index maps vocabulary items back to documents and offsets. Repeated terms produce multiple positions within one posting rather than duplicate document entries.

The construction cost is linear in total token count. This index supplies exact evidence for Boolean and phrase retrieval without assigning a relevance score.
