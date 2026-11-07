# Decode a CTC Alignment Path

CTC separates alignment length from output-token length. Several framewise alignments can therefore decode into the same shorter sequence.

A blank carries alignment information even though it disappears from the final text. In particular, it permits two consecutive copies of the same output label to be represented without collapsing into one.
