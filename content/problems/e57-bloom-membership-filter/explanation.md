# Inspect Bloom Filter False Positives

Bloom filters have no false negatives for correctly inserted items under a fixed hash mapping, but different items can collectively set all bits needed by a query.

The worked false-positive example separates the membership guarantee from exact storage. A positive result should trigger a definitive lookup when correctness requires certainty.

Concept references (original code and prose):

- [Bloom, Space/Time Trade-offs in Hash Coding with Allowable Errors](https://www.cs.princeton.edu/courses/archive/spr05/cos598E/bib/p422-bloom.pdf) — Boolean membership bits with supplied hashes; no deletion and no claimed false-positive rate.
