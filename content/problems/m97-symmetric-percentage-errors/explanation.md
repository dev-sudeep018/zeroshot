# Audit Relative Errors near Zero

Ordinary percentage error divides only by the actual value and becomes undefined near a zero target. This symmetric denominator makes the scale depend on both the target and prediction.

The measure is unchanged when actual and predicted are exchanged. It can still saturate at two for opposite signs, so it should be interpreted alongside errors in original units.
