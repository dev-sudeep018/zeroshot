# Reconcile Stock Requests

A sequence of requests shares state: an earlier fulfillment changes what later requests can receive. Taking min(requested, available) prevents negative stock and records shortages explicitly.

The output separates requested demand into filled and unfilled quantities. For each item, original stock equals remaining stock plus total fulfilled demand, which provides a useful conservation check.
