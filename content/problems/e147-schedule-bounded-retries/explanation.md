# Schedule Bounded Retries

Exponential backoff reduces repeated pressure after failed requests. A cap prevents the wait between later retries from increasing without bound.

This deterministic schedule omits jitter and request duration. Keeping those concerns separate makes the delay budget easy to verify and compose with a real retry system.
