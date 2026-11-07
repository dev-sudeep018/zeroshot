# Follow Mistakes through a Perceptron Pass

A perceptron adjusts its parameters only when the signed margin is nonpositive. The update moves the score in the direction of the correct label for the current feature vector.

This is one deterministic online pass, not training until convergence. Reordering the data may change the result because every prediction sees the model produced by earlier rows.
