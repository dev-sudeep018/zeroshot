# Deduplicate Idempotency Keys

Idempotency history prevents a replayed request from being applied twice while its key remains remembered. Bounded memory necessarily limits that protection.

The FIFO policy is defined by accepted requests, not all observed requests. An evicted key is accepted again, illustrating why durable idempotency stores use explicit retention guarantees.
