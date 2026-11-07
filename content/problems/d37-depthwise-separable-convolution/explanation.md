# Separate Spatial Filtering from Channel Mixing

The equivalent dense kernel is W[o,c,u,v]=pointwise_weights[o,c]\*depthwise_weights[c,u,v]. For a given input channel, every output uses a scaled version of the same spatial filter.

This factorization uses C*Kh*Kw+O*C weights instead of O*C*Kh*Kw. It changes expressiveness as well as parameter count; arbitrary dense kernels need not factor this way.

Adapted the upstream depthwise and pointwise operations to NumPy with explicit spatial slices. Removed singleton weight axes and retained valid stride-one cross-correlation semantics.

Adapted code source: https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/torch_judge/tasks/depthwise_conv.py
