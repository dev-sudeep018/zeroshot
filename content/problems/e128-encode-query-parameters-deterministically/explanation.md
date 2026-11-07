# Encode Query Parameters Deterministically

Deterministic query encoding helps compare URLs and generate repeatable requests. Sorting keys removes mapping insertion order while preserving repeated-value order.

An empty list contributes no pair, while an empty string contributes key=. These distinct states must not be collapsed by a truthiness check.
