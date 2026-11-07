# Flatten One Level of Records

One-level flattening removes transport batches while preserving the structure of each record. Recursive flattening would corrupt a record whose payload is itself a sequence.

The operation is an inverse of count-based batching when records are treated as indivisible items. Empty batches contribute no items and need no special placeholder.
