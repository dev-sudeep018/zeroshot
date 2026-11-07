# Merge Sorted Event Streams

Merging uses the fact that each source is already sorted. Only the two current front events need comparison, giving linear work in the total number of events.

A tie policy makes repeated timestamps reproducible. Left-first ordering is deliberate and must not be replaced by alphabetical ID order.
