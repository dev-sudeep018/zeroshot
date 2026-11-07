# Score Binary Features with Both Outcomes

Bernoulli naive Bayes models both whether a feature occurs and whether it does not. Omitting absent-feature terms changes the model and can reverse class preferences.

Log scores turn products of small conditional probabilities into sums. Their additive normalization is unnecessary when comparing classes, so this exercise returns the unnormalized scores.
