# Compare Forecast Errors with a Naive Baseline

A scaled error compares a forecast with the typical error of a seasonal-naive training baseline. Using evaluation observations to estimate that baseline would leak information into the reference scale.

The ratio is unit-free, but a perfectly constant seasonal training series has zero baseline error. A positive error cannot then be represented by a finite ratio, so the contract rejects that case explicitly.
