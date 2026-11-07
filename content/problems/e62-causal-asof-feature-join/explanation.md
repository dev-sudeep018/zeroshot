# Join Only Features Available at Prediction Time

A causal as-of join prevents temporal leakage by requiring every selected feature event to occur no later than the prediction query. Stable ordering gives a deterministic policy for repeated timestamps.

Event time is only one availability model. Real systems may also need ingestion-time constraints; this lesson makes its single-clock assumption explicit.

Concept references (original code and prose):

- [pandas merge_asof documentation](https://pandas.pydata.org/docs/reference/api/pandas.merge_asof.html) — Backward, exact-match-allowed single-clock join with stable last-row timestamp ties; no nearest/forward modes.
