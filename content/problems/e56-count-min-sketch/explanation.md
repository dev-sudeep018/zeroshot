# Estimate Frequencies with a Count-Min Sketch

With nonnegative increments, every queried counter includes the true frequency plus possible collision contributions. Taking the minimum cannot introduce an underestimate for a consistently hashed item.

Statistical error bounds require assumptions about the hash family and sketch dimensions. The lesson exposes supplied bucket mappings so collisions can be examined directly without claiming those probabilistic guarantees.

Concept references (original code and prose):

- [Cormode and Muthukrishnan, An Improved Data Stream Summary: The Count-Min Sketch and Its Applications](https://www.cs.ox.ac.uk/people/graham.cormode/pubs/html/CormodeMuthukrishnan04CMJalg.html) — Ordinary nonnegative counter updates with supplied hash buckets; no conservative updates or claimed error bound.
