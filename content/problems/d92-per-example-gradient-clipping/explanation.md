# Clip Individual Gradients before Averaging

Per-example clipping bounds how far one record can move the unaveraged update. Shorter gradients keep their full size and direction; longer gradients preserve direction but shrink to the norm limit.

The resulting mean is affected by the distribution of row lengths. Clipping the mean instead could hide opposing large contributions and is a different optimization operation.
