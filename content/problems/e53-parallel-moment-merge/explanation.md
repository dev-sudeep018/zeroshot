# Merge Statistics from Separate Partitions

Centered sums are measured around local means. A merged mean moves those centers, producing the between-partition correction in addition to the within-partition m2 totals.

The same sufficient statistics support streaming and distributed aggregation. In exact arithmetic merging is associative; floating-point order can cause small numerical differences.

Concept references (original code and prose):

- [Chan, Golub, and LeVeque, Algorithms for Computing the Sample Variance](https://www.tandfonline.com/doi/abs/10.1080/00031305.1983.10483115) — Pairwise moment merging with a between-partition correction; no raw-data reconstruction.
