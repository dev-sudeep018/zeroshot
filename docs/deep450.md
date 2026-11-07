# Deep-learning expansion D80-D129

This batch adds 50 original runnable lessons: 35 beginner and 15 intermediate, with 502 public cases. The beginner lessons assume basic Python and arrays and teach parameter budgets, training diagnostics, sequence preparation, image operations, and loss behavior. They are not syntax drills.

Each lesson contains three worked examples, starter guidance, a reference implementation, at least ten public cases, input validation, and an input-preservation check. Conceptual references are linked in attribution; prose, code, and fixtures are original. No third-party exercise statements or implementations were copied.

## Validation

- All 502 public cases pass against references; starters and trivial constant implementations are rejected.
- 27 independent numerical and combinatorial tests cover all 50 objectives. These include exact mask and receptive-field enumeration, finite-difference gradients, streaming equivalence, interpolation invariants, spectral gain, and network equivalence after folding or permutation.
- Worked outputs are Python literals with NumPy arrays displayed as lists and a rounding note.
- Full browser and release validation is recorded separately after integration.

## Lessons

| ID   | Level        | Objective                                                                                                                                                  |
| ---- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| D80  | beginner     | Return per-layer weight, bias, and total counts, plus the total network parameter count.                                                                   |
| D81  | beginner     | Count weight parameters, optional biases, and multiply-accumulates for one output image.                                                                   |
| D82  | beginner     | Trace theoretical receptive-field span and input-space jump after every layer.                                                                             |
| D83  | beginner     | Apply SGD only to trainable coordinates and report their changes.                                                                                          |
| D84  | beginner     | Compare Xavier and He weight variances and resulting pre-activation variances.                                                                             |
| D85  | beginner     | Return activity fractions, mean ReLU outputs, and batch inactivity flags.                                                                                  |
| D86  | beginner     | Compute probabilities, mean local derivatives, and saturation fractions per unit.                                                                          |
| D87  | beginner     | Return elementwise mean, variance, and second moment under independent inverted dropout.                                                                   |
| D88  | beginner     | Return the winning class, runner-up class, and logit margin for every example.                                                                             |
| D89  | beginner     | Average model probabilities and measure the fraction of votes outside the majority class.                                                                  |
| D90  | beginner     | Return each feature contribution and the resulting affine score for every example.                                                                         |
| D91  | beginner     | Return selected class scores, input gradients, and input-times-gradient attributions.                                                                      |
| D92  | intermediate | Clip every gradient row by its own L2 norm, then return the clipped rows, scale factors, and mean gradient.                                                |
| D93  | beginner     | Return cosine similarities and a boolean matrix identifying negative direction agreement, treating absolute cosine values at most 1e-12 as numerical zero. |
| D94  | beginner     | Return parameter norms, update norms, and stabilized update-to-weight ratios for each row.                                                                 |
| D95  | beginner     | Replay early stopping and return the best epoch, stopping epoch, and observed stall counts.                                                                |
| D96  | beginner     | Return the learning rate to use after each epoch’s validation, including repeated reductions down to a floor.                                              |
| D97  | beginner     | Return the proposed parameters and separate optimization and decay changes.                                                                                |
| D98  | beginner     | Return the lookahead point, new velocity, and updated parameters using the velocity-as-displacement convention.                                            |
| D99  | intermediate | Return the objective value, directional slope, directional curvature, and unconstrained minimizing step along the direction.                               |
| D100 | beginner     | Shift a padded token batch into aligned inputs and targets, and mark the valid prediction positions.                                                       |
| D101 | beginner     | Return per-token negative log likelihood with zeros at masked positions and its mean over valid positions.                                                 |
| D102 | beginner     | Build decoder input tokens, beginning with a start token and then selecting the previous gold or predicted token.                                          |
| D103 | beginner     | Merge consecutive identical path IDs, then remove blank IDs, returning the remaining token IDs.                                                            |
| D104 | beginner     | Gather one hidden vector per example using valid lengths, returning zeros for empty sequences.                                                             |
| D105 | beginner     | Return attention entropy in natural units, exponential effective support, and the largest weight per query.                                                |
| D106 | intermediate | Return layer-by-layer cumulative token mixing matrices after residual addition and row normalization.                                                      |
| D107 | intermediate | Compute outputs for the new chunk and return the history needed for the next call.                                                                         |
| D108 | intermediate | Extract valid image patches as flattened rows and return their top-left coordinates.                                                                       |
| D109 | beginner     | Perform a channel-first pixel shuffle without interpolation.                                                                                               |
| D110 | beginner     | Resize an integer label map with the documented nearest-neighbor coordinate rule.                                                                          |
| D111 | intermediate | Resize a single-channel image using bilinear interpolation with aligned corners.                                                                           |
| D112 | beginner     | Scatter pooled values to distinct flattened output indices and fill all other positions with zero.                                                         |
| D113 | intermediate | Average the documented floor-to-ceil regions for every output location.                                                                                    |
| D114 | beginner     | Return a boolean map marking pixels with at least one differently labeled four-connected in-bounds neighbor.                                               |
| D115 | beginner     | Return each heatmap’s total mass and mass-weighted center in zero-based row-column coordinates.                                                            |
| D116 | beginner     | Return the row-column coordinates and value of the first maximum in each heatmap.                                                                          |
| D117 | beginner     | Replace the pixels in a half-open rectangle with a fill value and return an erased-position mask.                                                          |
| D118 | beginner     | Replace a clipped rectangle of the first image with the second image and return the area-correct soft label.                                               |
| D119 | beginner     | Mix a feature batch and probability-label batch with a supplied partner permutation.                                                                       |
| D120 | beginner     | Scatter visible patch embeddings into their original positions and fill all other positions with a mask token.                                             |
| D121 | intermediate | Return the mean squared error over masked patch features and its gradient with respect to the prediction.                                                  |
| D122 | intermediate | Compute mean codebook and commitment losses with their separate gradients for already matched code vectors.                                                |
| D123 | intermediate | Scale a nonzero weight matrix so its largest singular value equals a requested positive bound.                                                             |
| D124 | intermediate | Return the squared Frobenius penalty on W.T@W-I and its gradient with respect to W.                                                                        |
| D125 | intermediate | Compute T-squared-scaled mean KL(teacher//student) and the gradient with respect to student logits.                                                        |
| D126 | intermediate | Return folded weights and bias for batch normalization applied to x@weights+bias.                                                                          |
| D127 | intermediate | Apply a hidden-neuron permutation to both sides of a two-layer network.                                                                                    |
| D128 | intermediate | Return mean negative log likelihood and the derivative with respect to temperature.                                                                        |
| D129 | beginner     | Return each residual’s Huber loss and derivative, plus the mean loss and the gradient of that mean.                                                        |

D93 now defines a 1e-12 numerical zero band for near-orthogonal cosine values and scales tiny nonzero gradients before normalization. The correction follows a native/WebAssembly reduction difference found by the full browser suite; independent and public cases cover both boundaries.
