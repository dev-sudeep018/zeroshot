# Carry a Causal Convolution across Chunks

A finite causal kernel needs only a fixed-length suffix of past input. Carrying that suffix makes chunk boundaries invisible to the mathematical operation.

Kernel orientation is easy to reverse accidentally: the first coefficient corresponds to the newest sample here. Keeping a clear state order enables independent streaming and full-sequence implementations to agree.
