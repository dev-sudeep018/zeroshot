# Compare Soft Teacher and Student Predictions

KL direction matters: the teacher distribution weights the comparison. A student matching the teacher exactly has zero loss and zero gradient at every supported temperature.

The T-squared multiplier is a training convention that compensates for much of the gradient shrinking caused by smoothing. The teacher logits are fixed targets in this exercise.
