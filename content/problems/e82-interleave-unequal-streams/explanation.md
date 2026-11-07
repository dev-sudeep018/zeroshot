# Interleave Unequal Streams

Round-wise interleaving combines sources fairly by position while preserving order within every source. It differs from ranked deduplication because repeated items remain legitimate occurrences.

The number of output items equals the sum of input stream lengths. Empty streams contribute nothing and should not terminate processing of other streams.
