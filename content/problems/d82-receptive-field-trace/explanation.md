# Trace a Stack’s Receptive Field

Composing local dependencies produces a larger receptive field. Jump tracks the spacing between consecutive output centers, so early strides magnify the effect of later kernels.

This theoretical span may contain gaps from dilation. It says which input range could matter, not that every location contributes equally on every example.
