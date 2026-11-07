# Split Work into Fixed Batches

Fixed batching bounds the number of records processed in one call. Unlike padded token batching, this contract ignores record sizes and partitions only by count.

Concatenating all output batches must recover the original item sequence. The final partial batch preserves records that would otherwise be lost by integer division.
