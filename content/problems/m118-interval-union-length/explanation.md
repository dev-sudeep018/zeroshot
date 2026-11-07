# Measure Covered Length without Double Counting

Adding interval lengths directly double-counts overlapping coverage. Merging first gives a disjoint representation whose lengths can be summed safely.

Touching endpoints occupy no extra length, but merging them produces a canonical connected representation. Degenerate point intervals can remain visible while contributing zero to total covered length.
