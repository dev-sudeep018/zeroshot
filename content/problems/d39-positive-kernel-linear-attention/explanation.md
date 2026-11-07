# Reassociate Attention through a Positive Kernel

Without epsilon, the output is a normalized weighted sum with weights given by positive feature inner products. The additive epsilon slightly reduces the total weight, especially when the kernel mass is very small.

The feature map changes the attention rule. Reassociation is algebraically valid for this kernel, but it does not make the result equal to ordinary softmax attention.

Adapted the upstream associative ELU-plus-one attention and its additive 1e-6 denominator. Used direct exp(x) on the negative branch to avoid cancellation and masked branch evaluation to avoid positive exponential overflow.

Adapted code source: https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/torch_judge/tasks/linear_attention.py
