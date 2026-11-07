# Trace a Circuit Breaker

A circuit breaker stops forwarding requests after repeated failures. Its open state prevents a failing dependency from receiving every subsequent request.

This small state machine uses explicit reset events instead of timers or half-open probes. Tracing state after every event exposes off-by-one errors at the failure threshold.
