# Compare a Regressor with the Mean Baseline

R-squared compares a model with predicting the target mean for every observation. A negative value means the model has more squared error than that baseline.

Constant targets make the baseline error zero, so a convention is necessary. Keeping the convention explicit avoids accidental division by zero or a misleading infinite score.
