# Check Monotonic Event Times

Monotonicity audits identify records that arrive out of expected temporal order. Sorting first would hide the very issue the audit needs to expose.

A local decrease differs from being below the historical maximum. After one decrease, later increasing timestamps are valid adjacent transitions even if still below an earlier peak.
