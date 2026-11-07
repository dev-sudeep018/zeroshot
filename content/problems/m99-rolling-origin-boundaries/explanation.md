# Keep Forecast Training before Validation

Forecast evaluation must respect what information was available at each prediction time. Expanding-window splits represent repeated training on everything observed before a new validation horizon.

The stride controls how often the origin advances; it does not change the horizon. Distinguishing them allows overlapping evaluation windows while preserving the causal boundary within every split.
