# Budget Shared Convolution Weights

Sharing weights keeps parameter storage independent of image area. Computation still grows because each output position applies the same kernel.

Divisibility expresses valid grouping of channel connections. A depthwise layer uses one group per input channel, potentially with multiple outputs per group.
