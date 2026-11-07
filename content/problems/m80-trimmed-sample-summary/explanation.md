# Reduce Outlier Influence by Trimming

A trimmed mean reduces the influence of extreme observations by removing the same number from both sorted tails. It differs from clipping, which keeps all observations but changes extreme values.

The trim parameter counts observations per side. Returning retained values makes ties and the exact support of the estimate visible, and the nonempty constraint prevents an undefined mean.
