# Simulate Token-Bucket Admission

The capacity controls the maximum burst while refill rate controls replenishment over time. A long idle period cannot build unlimited credit because the balance is capped.

This simulation is deterministic and single-threaded. A real shared limiter needs atomic state updates and a defined clock policy to preserve the same admission semantics under concurrency.
