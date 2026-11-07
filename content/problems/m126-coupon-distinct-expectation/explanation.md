# Predict How Many Categories Will Be Seen

The number of distinct observed categories is a sum of presence indicators. Expected values add even though observing one category changes what other categories can have appeared in a fixed number of draws.

The unseen probability decays as (1-p)^n. Using log1p and expm1 helps retain small appearance probabilities without subtracting nearly equal floating-point numbers.
