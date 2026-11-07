# Predict Inverted Dropout Moments

Scaling survivors by the reciprocal keep probability preserves their expectation. This explains why evaluation can use the original activation without drawing masks.

The training distribution still differs from evaluation: smaller keep probability increases second moments and variance. Equal means do not imply equal noise or equal downstream nonlinear behavior.
