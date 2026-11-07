# Restore Max-Pooled Values at Saved Locations

Saved pooling switches preserve where the selected maxima came from. Unpooling can therefore produce a sparse spatial representation aligned with the earlier feature map.

Most source values were discarded during pooling and cannot be recovered. Zero-filled positions explicitly represent that missing information rather than an inverse of the entire pooling operation.
