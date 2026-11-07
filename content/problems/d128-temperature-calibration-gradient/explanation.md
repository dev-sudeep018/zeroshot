# Differentiate a Calibration Temperature

The temperature gradient compares the observed class score with the score expected under the current predicted distribution. Its sign indicates whether more or less smoothing would reduce this labeled loss locally.

This is a calibration calculation on supplied data. It does not guarantee calibrated probabilities on a shifted population, and optimization should use data separate from final evaluation.
