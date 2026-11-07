# The 450-question curriculum

This expansion adds 250 distinct runnable lessons to the previous 200, including 195 new beginner lessons. The published catalog contains 450 lessons (205 beginner) and one retrieval project checkpoint, with 4,762 public cases (2,518 new). The three full paths contain 159 / 129 / 162 mathematics/ML, deep-learning, and engineering lessons respectively.

Beginner means approachable work with real arrays, records, measurements, model inputs, and training decisions. The exercises assume basic Python. They do not count print exercises, renamed framework ports, or number-swapped variants as new objectives. Each addition has three concrete examples, progressive hints, an explanation, a scaffolded incomplete starter, an inspectable reference, and public checks.

## Finding a starting point

The beginner route at `/paths/start-here/` offers 18 selected starting points across records, measurements, and small neural networks. The library at `/beginner/` opens with the beginner filter selected. Both use the same lessons and local progress as the full paths; these views do not increase the lesson count. Links from the learning home, paths, and library make them discoverable.

## Authorship and review

The 250 additions contain original implementations, teaching prose, and fixtures. Packages identify original authorship and, where included, conceptual reading links. Reading links are not claims that code or exercise text was imported. Existing licensed adaptations retain their notices. The [complete inventory](../content/curriculum-450-inventory.json) records every new objective, level, prerequisite, and evaluator count.

Independent suites cover numerical identities, analytical or exhaustive oracles, data preservation, parsing boundaries, state transitions, and model-operation properties. Cross-batch checks align the three samples with the worked examples and reject fixed example answers on valid inputs. Exact executed release checks are recorded in [verification](verification.md).

The long-term target remains 2,000 learning activities. This milestone does not add account synchronization or production hosting.

## Mathematics and ML

| ID   | Objective                                                                                                                     | Level        | Cases | Helpful first |
| ---- | ----------------------------------------------------------------------------------------------------------------------------- | ------------ | ----: | ------------- |
| M60  | [Calibrate and Limit Sensor Channels](../content/problems/m60-calibrated-sensor-table/lesson.json)                            | beginner     |    10 | —             |
| M61  | [Summarize Only Observed Cells](../content/problems/m61-masked-column-summary/lesson.json)                                    | beginner     |    10 | —             |
| M62  | [Aggregate a Grid into Partial Blocks](../content/problems/m62-partial-grid-block-sums/lesson.json)                           | beginner     |    10 | —             |
| M63  | [Accumulate Repeated Grid Measurements](../content/problems/m63-coordinate-grid-accumulation/lesson.json)                     | beginner     |    10 | —             |
| M64  | [Pack a Symmetric Measurement Matrix](../content/problems/m64-symmetric-triangle-packing/lesson.json)                         | beginner     |    10 | —             |
| M65  | [Convert Counts into Conditional Rows](../content/problems/m65-conditional-count-table/lesson.json)                           | beginner     |    10 | —             |
| M66  | [Summarize a Matrix by Diagonal Offset](../content/problems/m66-matrix-diagonal-profile/lesson.json)                          | beginner     |    10 | —             |
| M67  | [Answer Rectangular Sum Queries](../content/problems/m67-rectangle-sum-queries/lesson.json)                                   | beginner     |    10 | —             |
| M68  | [Locate Pixels inside Image Tiles](../content/problems/m68-pixel-tile-coordinates/lesson.json)                                | beginner     |    10 | —             |
| M69  | [Build an Independence Baseline for a Table](../content/problems/m69-independent-expected-counts/lesson.json)                 | beginner     |    10 | —             |
| M70  | [Measure Four-Connected Grid Regions](../content/problems/m70-connected-grid-regions/lesson.json)                             | beginner     |    10 | —             |
| M71  | [Find Peaks without Double-Counting Plateaus](../content/problems/m71-plateau-peak-locations/lesson.json)                     | beginner     |    10 | —             |
| M72  | [Measure Change on an Uneven Time Grid](../content/problems/m72-irregular-sample-velocity/lesson.json)                        | beginner     |    10 | —             |
| M73  | [Smooth a Signal at Its Boundaries](../content/problems/m73-centered-window-smoothing/lesson.json)                            | beginner     |    10 | —             |
| M74  | [Separate a Forecast from Its Update](../content/problems/m74-one-step-smoothed-forecasts/lesson.json)                        | beginner     |    10 | —             |
| M75  | [Remove and Restore a Seasonal Lag](../content/problems/m75-seasonal-difference-reconstruction/lesson.json)                   | beginner     |    10 | —             |
| M76  | [Compare a Signal with Its Delayed Self](../content/problems/m76-lagged-signal-products/lesson.json)                          | beginner     |    10 | —             |
| M77  | [Find Sign Changes through Exact Zeros](../content/problems/m77-zero-crossing-brackets/lesson.json)                           | beginner     |    10 | —             |
| M78  | [Accumulate Area on an Uneven Grid](../content/problems/m78-signed-trapezoid-areas/lesson.json)                               | beginner     |    10 | —             |
| M79  | [Resample between Known Measurements](../content/problems/m79-piecewise-linear-resampling/lesson.json)                        | beginner     |    10 | —             |
| M80  | [Reduce Outlier Influence by Trimming](../content/problems/m80-trimmed-sample-summary/lesson.json)                            | beginner     |    10 | —             |
| M81  | [Flag Outliers Using Median Deviations](../content/problems/m81-median-deviation-flags/lesson.json)                           | beginner     |    10 | —             |
| M82  | [Explain Which Tail Contains an Outlier](../content/problems/m82-tukey-outlier-fences/lesson.json)                            | beginner     |    10 | —             |
| M83  | [Combine Multiplicative Growth Factors](../content/problems/m83-geometric-growth-summary/lesson.json)                         | beginner     |    10 | —             |
| M84  | [Average Rates over Equal Distances](../content/problems/m84-harmonic-rate-summary/lesson.json)                               | beginner     |    10 | —             |
| M85  | [Compare Typical and Peak Signal Size](../content/problems/m85-signal-crest-factor/lesson.json)                               | beginner     |    10 | —             |
| M86  | [Compare Dispersion across Units](../content/problems/m86-relative-dispersion/lesson.json)                                    | beginner     |    10 | —             |
| M87  | [Measure Asymmetry and Tail Shape](../content/problems/m87-central-shape-moments/lesson.json)                                 | intermediate |    10 | —             |
| M88  | [Make Histogram Areas Sum to One](../content/problems/m88-weighted-density-histogram/lesson.json)                             | beginner     |    10 | —             |
| M89  | [Transfer Histogram Mass to New Bins](../content/problems/m89-histogram-overlap-rebinning/lesson.json)                        | intermediate |    10 | —             |
| M90  | [Describe Concentration with a Lorenz Curve](../content/problems/m90-lorenz-curve-area/lesson.json)                           | beginner     |    10 | —             |
| M91  | [Report Every Most Frequent Value](../content/problems/m91-empirical-mode-ties/lesson.json)                                   | beginner     |    10 | —             |
| M92  | [Compute Every Leave-One-Out Mean](../content/problems/m92-leave-one-out-means/lesson.json)                                   | beginner     |    10 | —             |
| M93  | [Separate Within-Group Scatter from Group Means](../content/problems/m93-pooled-within-group-variance/lesson.json)            | beginner     |    10 | —             |
| M94  | [Partition Variation between Groups](../content/problems/m94-one-way-anova-sums/lesson.json)                                  | beginner     |    10 | —             |
| M95  | [Measure How Concentrated Weights Are](../content/problems/m95-weighted-effective-sample-size/lesson.json)                    | beginner     |    10 | —             |
| M96  | [Build a Bounded Interval for a Success Rate](../content/problems/m96-success-rate-wilson-interval/lesson.json)               | intermediate |    10 | —             |
| M97  | [Audit Relative Errors near Zero](../content/problems/m97-symmetric-percentage-errors/lesson.json)                            | beginner     |    10 | —             |
| M98  | [Compare Forecast Errors with a Naive Baseline](../content/problems/m98-scaled-forecast-error/lesson.json)                    | beginner     |    10 | —             |
| M99  | [Keep Forecast Training before Validation](../content/problems/m99-rolling-origin-boundaries/lesson.json)                     | beginner     |    10 | —             |
| M100 | [Find the Nearest Point on a Segment](../content/problems/m100-point-segment-projection/lesson.json)                          | beginner     |    10 | —             |
| M101 | [Measure Triangle Orientation and Size](../content/problems/m101-signed-triangle-area/lesson.json)                            | beginner     |    10 | —             |
| M102 | [Walk a Closed Polygon](../content/problems/m102-polygon-perimeter-area/lesson.json)                                          | beginner     |    10 | —             |
| M103 | [Measure Perpendicular Distance to a Line](../content/problems/m103-point-line-distance/lesson.json)                          | beginner     |    10 | —             |
| M104 | [Describe a Point Cloud with a Bounding Box](../content/problems/m104-point-cloud-bounds/lesson.json)                         | beginner     |    10 | —             |
| M105 | [Rotate Points around a Chosen Pivot](../content/problems/m105-rotate-around-pivot/lesson.json)                               | beginner     |    10 | —             |
| M106 | [Convert Cartesian Positions to Canonical Polar Form](../content/problems/m106-polar-coordinate-canonicalization/lesson.json) | beginner     |    10 | —             |
| M107 | [Locate a Point Relative to a Triangle](../content/problems/m107-barycentric-triangle-coordinates/lesson.json)                | intermediate |    10 | —             |
| M108 | [Intersect Two Nonparallel Segments](../content/problems/m108-segment-intersection-parameters/lesson.json)                    | intermediate |    10 | —             |
| M109 | [Reflect Points across an Implicit Line](../content/problems/m109-reflection-across-line/lesson.json)                         | beginner     |    10 | —             |
| M110 | [Clip a Segment to a Rectangle](../content/problems/m110-axis-aligned-box-clipping/lesson.json)                               | intermediate |    10 | —             |
| M111 | [Sample a Path by Traveled Distance](../content/problems/m111-polyline-distance-resampling/lesson.json)                       | beginner     |    10 | —             |
| M112 | [Split a Vector into Parallel and Perpendicular Parts](../content/problems/m112-orthogonal-vector-components/lesson.json)     | beginner     |    10 | —             |
| M113 | [Construct an Oriented Plane from Three Points](../content/problems/m113-plane-from-three-points/lesson.json)                 | intermediate |    10 | —             |
| M114 | [Rotate a 3D Vector around an Axis](../content/problems/m114-axis-angle-rotation/lesson.json)                                 | intermediate |    10 | —             |
| M115 | [Classify Points against a Polygon Boundary](../content/problems/m115-point-in-simple-polygon/lesson.json)                    | beginner     |    10 | —             |
| M116 | [Recover a Triangle from Side Lengths](../content/problems/m116-cosine-rule-triangle/lesson.json)                             | beginner     |    10 | —             |
| M117 | [Summarize a Planar Mass Distribution](../content/problems/m117-point-cloud-inertia/lesson.json)                              | intermediate |    10 | —             |
| M118 | [Measure Covered Length without Double Counting](../content/problems/m118-interval-union-length/lesson.json)                  | beginner     |    10 | —             |
| M119 | [Measure Overlap between Two Disks](../content/problems/m119-circle-circle-overlap/lesson.json)                               | intermediate |    10 | —             |
| M120 | [Combine Events in a Finite Sample Space](../content/problems/m120-finite-event-probability/lesson.json)                      | beginner     |    10 | —             |
| M121 | [Combine Independent Discrete Measurements](../content/problems/m121-independent-sum-distribution/lesson.json)                | beginner     |    10 | —             |
| M122 | [Count Successes in a Sample without Replacement](../content/problems/m122-sampling-without-replacement/lesson.json)          | beginner     |    10 | —             |
| M123 | [Track the First Success before a Deadline](../content/problems/m123-first-success-waiting/lesson.json)                       | beginner     |    10 | —             |
| M124 | [Count Events under a Poisson Model](../content/problems/m124-poisson-event-probabilities/lesson.json)                        | beginner     |    10 | —             |
| M125 | [Turn Fixed Uniform Draws into Categories](../content/problems/m125-discrete-inverse-cdf/lesson.json)                         | beginner     |    10 | —             |
| M126 | [Predict How Many Categories Will Be Seen](../content/problems/m126-coupon-distinct-expectation/lesson.json)                  | beginner     |    10 | —             |
| M127 | [Find the Chance of a Repeated Label](../content/problems/m127-birthday-collision-probability/lesson.json)                    | beginner     |    10 | —             |
| M128 | [Combine Three Overlapping Events](../content/problems/m128-inclusion-exclusion-three-events/lesson.json)                     | intermediate |    10 | —             |
| M129 | [Condition a Joint Table on Selected Columns](../content/problems/m129-conditional-table-distribution/lesson.json)            | beginner     |    10 | —             |
| M130 | [Separate Within-Case and Between-Case Uncertainty](../content/problems/m130-law-total-variance/lesson.json)                  | beginner     |    10 | —             |
| M131 | [Move Probability through a Transition Table](../content/problems/m131-markov-distribution-steps/lesson.json)                 | beginner     |    10 | —             |
| M132 | [Track Survival before an Absorbing State](../content/problems/m132-absorbing-chain-survival/lesson.json)                     | intermediate |    10 | —             |
| M133 | [Separate No Event, One Event and Several Events](../content/problems/m133-competing-independent-events/lesson.json)          | beginner     |    10 | —             |
| M134 | [Count Dice Outcomes before Normalizing](../content/problems/m134-fair-dice-sum-counts/lesson.json)                           | beginner     |    11 | —             |
| M135 | [Decode a Combination from Its Lexicographic Rank](../content/problems/m135-combinations-by-rank/lesson.json)                 | intermediate |    10 | —             |
| M136 | [Measure Disorder in a Permutation](../content/problems/m136-permutation-inversion-count/lesson.json)                         | beginner     |    10 | —             |
| M137 | [Count Monotone Routes around Blocked Cells](../content/problems/m137-lattice-path-counts/lesson.json)                        | beginner     |    11 | —             |
| M138 | [Count Assignments with No Fixed Points](../content/problems/m138-derangement-counts/lesson.json)                             | beginner     |    11 | —             |
| M139 | [Estimate How Many Boxes Stay Empty](../content/problems/m139-occupancy-empty-boxes/lesson.json)                              | intermediate |    10 | —             |
| M140 | [Evaluate a Polynomial and Its Slope Together](../content/problems/m140-polynomial-horner-derivative/lesson.json)             | beginner     |    10 | —             |
| M141 | [Integrate a Polynomial between Bounds](../content/problems/m141-polynomial-antiderivative-area/lesson.json)                  | beginner     |    10 | —             |
| M142 | [Keep a Root inside a Shrinking Bracket](../content/problems/m142-bisection-polynomial-root/lesson.json)                      | intermediate |    12 | —             |
| M143 | [Trace Newton Updates toward a Square Root](../content/problems/m143-newton-square-root-trace/lesson.json)                    | beginner     |    10 | —             |
| M144 | [Integrate Evenly Spaced Samples with Simpson Weights](../content/problems/m144-composite-simpson-area/lesson.json)           | beginner     |    10 | —             |
| M145 | [Recover a Quadratic through Three Samples](../content/problems/m145-quadratic-interpolation/lesson.json)                     | beginner     |    10 | —             |
| M146 | [Step through a First-Order Cooling Model](../content/problems/m146-euler-cooling-trajectory/lesson.json)                     | beginner     |    10 | —             |
| M147 | [Update a Root Estimate from Two Function Values](../content/problems/m147-secant-polynomial-root/lesson.json)                | intermediate |    10 | —             |
| M148 | [Update a Linear Solve without Reusing New Values](../content/problems/m148-jacobi-linear-iteration/lesson.json)              | intermediate |    10 | —             |
| M149 | [Solve a Small System with Partial Pivoting](../content/problems/m149-gaussian-elimination-pivot/lesson.json)                 | intermediate |    10 | —             |
| M150 | [Score Binary Features with Both Outcomes](../content/problems/m150-bernoulli-naive-bayes-scores/lesson.json)                 | intermediate |    10 | —             |
| M151 | [Fit a Line and Explain Its Residuals](../content/problems/m151-least-squares-line-fit/lesson.json)                           | beginner     |    10 | —             |
| M152 | [Compare a Regressor with the Mean Baseline](../content/problems/m152-regression-r-squared/lesson.json)                       | beginner     |    11 | —             |
| M153 | [Ignore Errors inside a Tolerance Band](../content/problems/m153-epsilon-insensitive-error/lesson.json)                       | beginner     |    10 | —             |
| M154 | [Compare Agreement with Its Chance Baseline](../content/problems/m154-cohen-label-agreement/lesson.json)                      | beginner     |    10 | —             |
| M155 | [Give Each Class Equal Total Training Weight](../content/problems/m155-class-balanced-sample-weights/lesson.json)             | beginner     |    10 | —             |
| M156 | [Classify by Learned Class Means](../content/problems/m156-nearest-centroid-classifier/lesson.json)                           | beginner     |    10 | —             |
| M157 | [Predict from Ordered Regression Bins](../content/problems/m157-piecewise-constant-regression/lesson.json)                    | beginner     |    10 | —             |
| M158 | [Minimize One Ridge Coordinate Exactly](../content/problems/m158-ridge-single-coordinate-update/lesson.json)                  | intermediate |    10 | —             |
| M159 | [Find a Median under Unequal Observation Weights](../content/problems/m159-weighted-median-selection/lesson.json)             | beginner     |    10 | —             |

## Deep learning

| ID   | Objective                                                                                                                     | Level        | Cases | Helpful first |
| ---- | ----------------------------------------------------------------------------------------------------------------------------- | ------------ | ----: | ------------- |
| D80  | [Count Parameters across a Dense Network](../content/problems/d80-dense-parameter-budget/lesson.json)                         | beginner     |    10 | —             |
| D81  | [Budget Shared Convolution Weights](../content/problems/d81-grouped-convolution-budget/lesson.json)                           | beginner     |    10 | —             |
| D82  | [Trace a Stack’s Receptive Field](../content/problems/d82-receptive-field-trace/lesson.json)                                  | beginner     |    10 | —             |
| D83  | [Respect Frozen Parameters during SGD](../content/problems/d83-frozen-parameter-step/lesson.json)                             | beginner     |    10 | —             |
| D84  | [Compare Fan-Based Initialization Scales](../content/problems/d84-initialization-variance-budget/lesson.json)                 | beginner     |    10 | —             |
| D85  | [Find Inactive ReLU Neurons](../content/problems/d85-relu-activity-audit/lesson.json)                                         | beginner     |    10 | D05           |
| D86  | [Audit Sigmoid Saturation](../content/problems/d86-sigmoid-saturation-audit/lesson.json)                                      | beginner     |    10 | D08           |
| D87  | [Predict Inverted Dropout Moments](../content/problems/d87-dropout-moment-prediction/lesson.json)                             | beginner     |    10 | D06           |
| D88  | [Interpret the Top Two Class Scores](../content/problems/d88-classifier-logit-margins/lesson.json)                            | beginner     |    10 | —             |
| D89  | [Compare Ensemble Probabilities and Votes](../content/problems/d89-ensemble-vote-disagreement/lesson.json)                    | beginner     |    10 | —             |
| D90  | [Explain a Neuron through Feature Contributions](../content/problems/d90-affine-feature-contributions/lesson.json)            | beginner     |    10 | —             |
| D91  | [Trace a Class Score Back to Input Features](../content/problems/d91-linear-input-saliency/lesson.json)                       | beginner     |    10 | D90           |
| D92  | [Clip Individual Gradients before Averaging](../content/problems/d92-per-example-gradient-clipping/lesson.json)               | intermediate |    10 | —             |
| D93  | [Detect Conflicting Task Gradients](../content/problems/d93-gradient-conflict-audit/lesson.json)                              | beginner     |    12 | —             |
| D94  | [Compare Update Size with Parameter Scale](../content/problems/d94-relative-parameter-update-audit/lesson.json)               | beginner     |    10 | —             |
| D95  | [Stop Training after Sustained Validation Stalls](../content/problems/d95-early-stopping-trace/lesson.json)                   | beginner     |    10 | —             |
| D96  | [Reduce Learning Rate on a Validation Plateau](../content/problems/d96-plateau-learning-rate-trace/lesson.json)               | beginner     |    10 | —             |
| D97  | [Apply Weight Decay Separately from the Optimizer Direction](../content/problems/d97-decoupled-weight-decay-step/lesson.json) | beginner     |    10 | —             |
| D98  | [Update Momentum from a Lookahead Gradient](../content/problems/d98-nesterov-velocity-update/lesson.json)                     | beginner     |    10 | —             |
| D99  | [Probe Curvature along an Optimization Direction](../content/problems/d99-quadratic-directional-curvature/lesson.json)        | intermediate |    10 | —             |
| D100 | [Build Next-Token Training Pairs](../content/problems/d100-shifted-language-model-batch/lesson.json)                          | beginner     |    10 | —             |
| D101 | [Average Loss over Real Tokens Only](../content/problems/d101-masked-token-negative-log-likelihood/lesson.json)               | beginner     |    10 | D100          |
| D102 | [Choose Decoder Inputs with Scheduled Teacher Forcing](../content/problems/d102-scheduled-teacher-forcing-inputs/lesson.json) | beginner     |    10 | D100          |
| D103 | [Decode a CTC Alignment Path](../content/problems/d103-ctc-path-collapse/lesson.json)                                         | beginner     |    10 | —             |
| D104 | [Gather the Final Real Sequence State](../content/problems/d104-last-valid-hidden-state/lesson.json)                          | beginner     |    10 | —             |
| D105 | [Measure How Broadly Attention Is Spread](../content/problems/d105-attention-effective-support/lesson.json)                   | beginner     |    10 | —             |
| D106 | [Compose Residual Attention across Layers](../content/problems/d106-residual-attention-rollout/lesson.json)                   | intermediate |    10 | —             |
| D107 | [Carry a Causal Convolution across Chunks](../content/problems/d107-streaming-causal-convolution/lesson.json)                 | intermediate |    10 | —             |
| D108 | [Turn Image Windows into Matrix Rows](../content/problems/d108-image-to-patch-matrix/lesson.json)                             | intermediate |    10 | —             |
| D109 | [Move Subpixel Channels into Image Space](../content/problems/d109-pixel-shuffle-upscaling/lesson.json)                       | beginner     |    10 | —             |
| D110 | [Resize Class Labels without Inventing Classes](../content/problems/d110-nearest-segmentation-resize/lesson.json)             | beginner     |    10 | —             |
| D111 | [Interpolate an Image with Aligned Corners](../content/problems/d111-bilinear-align-corners-resize/lesson.json)               | intermediate |    10 | —             |
| D112 | [Restore Max-Pooled Values at Saved Locations](../content/problems/d112-switch-guided-max-unpool/lesson.json)                 | beginner     |    10 | —             |
| D113 | [Pool an Image into a Requested Grid](../content/problems/d113-adaptive-spatial-average-pooling/lesson.json)                  | intermediate |    10 | —             |
| D114 | [Mark Boundaries between Segmentation Regions](../content/problems/d114-segmentation-boundary-map/lesson.json)                | beginner     |    10 | —             |
| D115 | [Locate a Landmark from All Heatmap Mass](../content/problems/d115-heatmap-center-of-mass/lesson.json)                        | beginner     |    10 | —             |
| D116 | [Decode the Strongest Heatmap Location](../content/problems/d116-heatmap-peak-coordinates/lesson.json)                        | beginner     |    10 | —             |
| D117 | [Erase a Clipped Image Rectangle](../content/problems/d117-rectangle-erasing-augmentation/lesson.json)                        | beginner     |    10 | —             |
| D118 | [Mix Labels Using the Actual CutMix Area](../content/problems/d118-cutmix-effective-area/lesson.json)                         | beginner     |    10 | D117          |
| D119 | [Interpolate Training Examples and Their Labels Together](../content/problems/d119-paired-batch-mixup/lesson.json)            | beginner     |    10 | —             |
| D120 | [Restore Visible Patches to Their Original Positions](../content/problems/d120-restore-masked-patch-order/lesson.json)        | beginner     |    10 | —             |
| D121 | [Restrict Reconstruction Loss to Masked Patches](../content/problems/d121-masked-reconstruction-objective/lesson.json)        | intermediate |    10 | D120          |
| D122 | [Separate Codebook and Commitment Gradients](../content/problems/d122-vector-quantization-loss-gradients/lesson.json)         | intermediate |    10 | —             |
| D123 | [Control a Linear Layer’s Maximum Gain](../content/problems/d123-spectral-weight-normalization/lesson.json)                   | intermediate |    10 | —             |
| D124 | [Differentiate an Orthogonality Penalty](../content/problems/d124-orthogonal-column-penalty/lesson.json)                      | intermediate |    10 | —             |
| D125 | [Compare Soft Teacher and Student Predictions](../content/problems/d125-temperature-distillation-kl/lesson.json)              | intermediate |    10 | —             |
| D126 | [Fold Evaluation Batch Normalization into a Linear Layer](../content/problems/d126-fold-batchnorm-affine/lesson.json)         | intermediate |    10 | —             |
| D127 | [Reorder Hidden Neurons without Changing a Network](../content/problems/d127-hidden-neuron-permutation/lesson.json)           | intermediate |    10 | —             |
| D128 | [Differentiate a Calibration Temperature](../content/problems/d128-temperature-calibration-gradient/lesson.json)              | intermediate |    10 | —             |
| D129 | [Limit Outlier Influence with Huber Loss](../content/problems/d129-huber-residual-gradient/lesson.json)                       | beginner     |    10 | —             |

## Practical engineering

| ID   | Objective                                                                                                                         | Level        | Cases | Helpful first |
| ---- | --------------------------------------------------------------------------------------------------------------------------------- | ------------ | ----: | ------------- |
| E63  | [Normalize and Deduplicate Tags](../content/problems/e63-normalize-and-deduplicate-tags/lesson.json)                              | beginner     |    10 | —             |
| E64  | [Route Support Tickets](../content/problems/e64-route-support-tickets/lesson.json)                                                | beginner     |    10 | —             |
| E65  | [Reconcile Stock Requests](../content/problems/e65-reconcile-stock-requests/lesson.json)                                          | beginner     |    10 | E64           |
| E66  | [Summarize Completed Orders](../content/problems/e66-summarize-completed-orders/lesson.json)                                      | beginner     |    10 | E64           |
| E67  | [Apply Sequential Balance Changes](../content/problems/e67-apply-sequential-balance-changes/lesson.json)                          | beginner     |    10 | —             |
| E68  | [Find the First Matching Record](../content/problems/e68-find-the-first-matching-record/lesson.json)                              | beginner     |    10 | —             |
| E69  | [Extract Optional Record Fields](../content/problems/e69-extract-optional-record-fields/lesson.json)                              | beginner     |    10 | E68           |
| E70  | [Project Records to a Schema](../content/problems/e70-project-records-to-a-schema/lesson.json)                                    | beginner     |    10 | E69           |
| E71  | [Rename Record Fields Safely](../content/problems/e71-rename-record-fields-safely/lesson.json)                                    | beginner     |    10 | E70           |
| E72  | [Index Unique Records](../content/problems/e72-index-unique-records/lesson.json)                                                  | beginner     |    10 | E68           |
| E73  | [Group Records by Category](../content/problems/e73-group-records-by-category/lesson.json)                                        | beginner     |    10 | E72           |
| E74  | [Deduplicate Records by Latest Position](../content/problems/e74-deduplicate-records-by-latest-position/lesson.json)              | beginner     |    10 | E72           |
| E75  | [Compare Two Inventories](../content/problems/e75-compare-two-inventories/lesson.json)                                            | beginner     |    10 | E72           |
| E76  | [Merge Configuration Layers](../content/problems/e76-merge-configuration-layers/lesson.json)                                      | beginner     |    10 | —             |
| E77  | [Resolve Configuration Defaults](../content/problems/e77-resolve-configuration-defaults/lesson.json)                              | beginner     |    10 | E76           |
| E78  | [Invert a Many-to-One Lookup](../content/problems/e78-invert-a-many-to-one-lookup/lesson.json)                                    | beginner     |    10 | E73           |
| E79  | [Allocate Round-Robin Work](../content/problems/e79-allocate-round-robin-work/lesson.json)                                        | beginner     |    10 | —             |
| E80  | [Split Work into Fixed Batches](../content/problems/e80-split-work-into-fixed-batches/lesson.json)                                | beginner     |    10 | —             |
| E81  | [Paginate Records with Metadata](../content/problems/e81-paginate-records-with-metadata/lesson.json)                              | beginner     |    10 | E80           |
| E82  | [Interleave Unequal Streams](../content/problems/e82-interleave-unequal-streams/lesson.json)                                      | beginner     |    10 | E79           |
| E83  | [Flatten One Level of Records](../content/problems/e83-flatten-one-level-of-records/lesson.json)                                  | beginner     |    10 | E80           |
| E84  | [Expand Repeated Job Requests](../content/problems/e84-expand-repeated-job-requests/lesson.json)                                  | beginner     |    10 | —             |
| E85  | [Count Adjacent Status Transitions](../content/problems/e85-count-adjacent-status-transitions/lesson.json)                        | beginner     |    10 | —             |
| E86  | [Summarize Streak Lengths by Status](../content/problems/e86-summarize-streak-lengths-by-status/lesson.json)                      | beginner     |    10 | E85           |
| E87  | [Find Gaps in Sequence Numbers](../content/problems/e87-find-gaps-in-sequence-numbers/lesson.json)                                | beginner     |    10 | —             |
| E88  | [Audit Duplicate Identifiers](../content/problems/e88-audit-duplicate-identifiers/lesson.json)                                    | beginner     |    10 | E72           |
| E89  | [Match Ordered IDs to Records](../content/problems/e89-match-ordered-ids-to-records/lesson.json)                                  | beginner     |    10 | E72           |
| E90  | [Zip Unequal Columns Explicitly](../content/problems/e90-zip-unequal-columns-explicitly/lesson.json)                              | beginner     |    10 | —             |
| E91  | [Unzip Record Columns](../content/problems/e91-unzip-record-columns/lesson.json)                                                  | beginner     |    10 | E70           |
| E92  | [Build a Multi-Key Stable Sort](../content/problems/e92-build-a-multi-key-stable-sort/lesson.json)                                | beginner     |    10 | —             |
| E93  | [Select the Best Record Per Group](../content/problems/e93-select-the-best-record-per-group/lesson.json)                          | beginner     |    10 | E73           |
| E94  | [Filter Records by Inclusive Ranges](../content/problems/e94-filter-records-by-inclusive-ranges/lesson.json)                      | beginner     |    10 | —             |
| E95  | [Report Field-Level Changes](../content/problems/e95-report-field-level-changes/lesson.json)                                      | beginner     |    10 | E75           |
| E96  | [Apply Explicit Record Patches](../content/problems/e96-apply-explicit-record-patches/lesson.json)                                | beginner     |    10 | E76, E95      |
| E97  | [Build a Quantity Histogram](../content/problems/e97-build-a-quantity-histogram/lesson.json)                                      | beginner     |    10 | —             |
| E98  | [Validate a Required-Field Schema](../content/problems/e98-validate-a-required-field-schema/lesson.json)                          | beginner     |    10 | E70           |
| E99  | [Validate Foreign-Key References](../content/problems/e99-validate-foreign-key-references/lesson.json)                            | beginner     |    10 | E72, E98      |
| E100 | [Reconcile Ordered Membership Lists](../content/problems/e100-reconcile-ordered-membership-lists/lesson.json)                     | beginner     |    10 | —             |
| E101 | [Merge Sorted Event Streams](../content/problems/e101-merge-sorted-event-streams/lesson.json)                                     | beginner     |    10 | —             |
| E102 | [Track Open and Closed Tasks](../content/problems/e102-track-open-and-closed-tasks/lesson.json)                                   | beginner     |    10 | E85           |
| E103 | [Normalize Whitespace in Text](../content/problems/e103-normalize-whitespace-in-text/lesson.json)                                 | beginner     |    10 | —             |
| E104 | [Tokenize ASCII Words with Offsets](../content/problems/e104-tokenize-ascii-words-with-offsets/lesson.json)                       | beginner     |    10 | —             |
| E105 | [Replace Whole Tokens from a Glossary](../content/problems/e105-replace-whole-tokens-from-a-glossary/lesson.json)                 | beginner     |    10 | E103          |
| E106 | [Redact Explicit Character Spans](../content/problems/e106-redact-explicit-character-spans/lesson.json)                           | beginner     |    10 | E104          |
| E107 | [Extract Bounded Context Windows](../content/problems/e107-extract-bounded-context-windows/lesson.json)                           | beginner     |    10 | E104          |
| E108 | [Match Case-Insensitive Exact Answers](../content/problems/e108-match-case-insensitive-exact-answers/lesson.json)                 | beginner     |    10 | E103          |
| E109 | [Count Unique Terms Per Document](../content/problems/e109-count-unique-terms-per-document/lesson.json)                           | beginner     |    10 | —             |
| E110 | [Filter Stopwords Without Reordering](../content/problems/e110-filter-stopwords-without-reordering/lesson.json)                   | beginner     |    10 | —             |
| E111 | [Build UTF-8 Character Offset Maps](../content/problems/e111-build-utf-8-character-offset-maps/lesson.json)                       | beginner     |    10 | E104          |
| E112 | [Encode Tokens with an Unknown ID](../content/problems/e112-encode-tokens-with-an-unknown-id/lesson.json)                         | beginner     |    10 | —             |
| E113 | [Decode Token IDs with Explicit Fallback](../content/problems/e113-decode-token-ids-with-explicit-fallback/lesson.json)           | beginner     |    10 | E112          |
| E114 | [Measure Truncation of Token Sequences](../content/problems/e114-measure-truncation-of-token-sequences/lesson.json)               | beginner     |    10 | —             |
| E115 | [Validate BIO Entity Tag Transitions](../content/problems/e115-validate-bio-entity-tag-transitions/lesson.json)                   | beginner     |    10 | —             |
| E116 | [Read Simple Key-Value Lines](../content/problems/e116-read-simple-key-value-lines/lesson.json)                                   | beginner     |    10 | —             |
| E117 | [Parse Strict Boolean Settings](../content/problems/e117-parse-strict-boolean-settings/lesson.json)                               | beginner     |    10 | —             |
| E118 | [Parse Bounded Decimal Integers](../content/problems/e118-parse-bounded-decimal-integers/lesson.json)                             | beginner     |    11 | —             |
| E119 | [Parse Durations with Explicit Units](../content/problems/e119-parse-durations-with-explicit-units/lesson.json)                   | beginner     |    10 | E118          |
| E120 | [Parse Semantic Version Triples](../content/problems/e120-parse-semantic-version-triples/lesson.json)                             | beginner     |    10 | E118          |
| E121 | [Parse CSV Records by Header](../content/problems/e121-parse-csv-records-by-header/lesson.json)                                   | beginner     |    11 | —             |
| E122 | [Serialize CSV Records in Schema Order](../content/problems/e122-serialize-csv-records-in-schema-order/lesson.json)               | beginner     |    11 | E121          |
| E123 | [Parse JSON Lines with Error Positions](../content/problems/e123-parse-json-lines-with-error-positions/lesson.json)               | beginner     |    10 | —             |
| E124 | [Canonicalize JSON for Cache Keys](../content/problems/e124-canonicalize-json-for-cache-keys/lesson.json)                         | beginner     |    10 | —             |
| E125 | [Validate an ASCII Slug](../content/problems/e125-validate-an-ascii-slug/lesson.json)                                             | beginner     |    10 | —             |
| E126 | [Normalize Relative Resource Paths](../content/problems/e126-normalize-relative-resource-paths/lesson.json)                       | beginner     |    11 | —             |
| E127 | [Parse URL Query Pairs](../content/problems/e127-parse-url-query-pairs/lesson.json)                                               | beginner     |    11 | —             |
| E128 | [Encode Query Parameters Deterministically](../content/problems/e128-encode-query-parameters-deterministically/lesson.json)       | beginner     |    10 | E127          |
| E129 | [Audit Tabular Row Widths](../content/problems/e129-audit-tabular-row-widths/lesson.json)                                         | beginner     |    10 | —             |
| E130 | [Detect Mixed Primitive Column Types](../content/problems/e130-detect-mixed-primitive-column-types/lesson.json)                   | beginner     |    10 | —             |
| E131 | [Find Blank and Missing Cells](../content/problems/e131-find-blank-and-missing-cells/lesson.json)                                 | beginner     |    10 | —             |
| E132 | [Check Monotonic Event Times](../content/problems/e132-check-monotonic-event-times/lesson.json)                                   | beginner     |    10 | —             |
| E133 | [Validate Unique Composite Keys](../content/problems/e133-validate-unique-composite-keys/lesson.json)                             | beginner     |    10 | E88           |
| E134 | [Forward-Fill Missing Values with a Limit](../content/problems/e134-forward-fill-missing-values-with-a-limit/lesson.json)         | beginner     |    10 | —             |
| E135 | [Check Allowed Category Values](../content/problems/e135-check-allowed-category-values/lesson.json)                               | beginner     |    10 | —             |
| E136 | [Apply Training Category Maps](../content/problems/e136-apply-training-category-maps/lesson.json)                                 | beginner     |    10 | E112          |
| E137 | [Summarize Rule-Based Data Quality](../content/problems/e137-summarize-rule-based-data-quality/lesson.json)                       | beginner     |    10 | E98, E94      |
| E138 | [Audit Multilabel Hamming Errors](../content/problems/e138-audit-multilabel-hamming-errors/lesson.json)                           | beginner     |    11 | —             |
| E139 | [Score Exact-Match Predictions by Group](../content/problems/e139-score-exact-match-predictions-by-group/lesson.json)             | beginner     |    10 | —             |
| E140 | [Compute Retrieval Precision at a Cutoff](../content/problems/e140-compute-retrieval-precision-at-a-cutoff/lesson.json)           | beginner     |    10 | —             |
| E141 | [Measure Ranking Coverage Across Queries](../content/problems/e141-measure-ranking-coverage-across-queries/lesson.json)           | beginner     |    10 | —             |
| E142 | [Find Pairwise Result-Set Disagreements](../content/problems/e142-find-pairwise-result-set-disagreements/lesson.json)             | beginner     |    10 | —             |
| E143 | [Build Deterministic Holdout by ID Hash](../content/problems/e143-build-deterministic-holdout-by-id-hash/lesson.json)             | intermediate |    13 | —             |
| E144 | [Assign Events to Fixed Time Windows](../content/problems/e144-assign-events-to-fixed-time-windows/lesson.json)                   | intermediate |    10 | —             |
| E145 | [Sessionize Events by Inactivity](../content/problems/e145-sessionize-events-by-inactivity/lesson.json)                           | intermediate |    10 | —             |
| E146 | [Deduplicate Idempotency Keys](../content/problems/e146-deduplicate-idempotency-keys/lesson.json)                                 | intermediate |    10 | —             |
| E147 | [Schedule Bounded Retries](../content/problems/e147-schedule-bounded-retries/lesson.json)                                         | intermediate |    10 | —             |
| E148 | [Trace a Circuit Breaker](../content/problems/e148-trace-a-circuit-breaker/lesson.json)                                           | intermediate |    10 | —             |
| E149 | [Simulate a FIFO Work Queue](../content/problems/e149-simulate-a-fifo-work-queue/lesson.json)                                     | intermediate |    10 | —             |
| E150 | [Simulate a Bounded Priority Queue](../content/problems/e150-simulate-a-bounded-priority-queue/lesson.json)                       | intermediate |    10 | —             |
| E151 | [Compute Worker Makespan](../content/problems/e151-compute-worker-makespan/lesson.json)                                           | intermediate |    10 | —             |
| E152 | [Select Jobs by Dependencies](../content/problems/e152-select-jobs-by-dependencies/lesson.json)                                   | intermediate |    10 | —             |
| E153 | [Find Transitive Dependency Impact](../content/problems/e153-find-transitive-dependency-impact/lesson.json)                       | intermediate |    10 | —             |
| E154 | [Build a Prefix Search Index](../content/problems/e154-build-a-prefix-search-index/lesson.json)                                   | intermediate |    10 | —             |
| E155 | [Match Multiword Phrases Exactly](../content/problems/e155-match-multiword-phrases-exactly/lesson.json)                           | intermediate |    10 | —             |
| E156 | [Segment Sentences with a Small State Machine](../content/problems/e156-segment-sentences-with-a-small-state-machine/lesson.json) | intermediate |    10 | —             |
| E157 | [Budget Messages by UTF-8 Bytes](../content/problems/e157-budget-messages-by-utf-8-bytes/lesson.json)                             | intermediate |    10 | —             |
| E158 | [Build Reversible Length-Prefixed Frames](../content/problems/e158-build-reversible-length-prefixed-frames/lesson.json)           | intermediate |    11 | —             |
| E159 | [Verify Payload Digests](../content/problems/e159-verify-payload-digests/lesson.json)                                             | intermediate |    10 | —             |
| E160 | [Apply a Versioned Cache Policy](../content/problems/e160-apply-a-versioned-cache-policy/lesson.json)                             | intermediate |    10 | —             |
| E161 | [Reconcile Append-Only Checkpoints](../content/problems/e161-reconcile-append-only-checkpoints/lesson.json)                       | intermediate |    10 | —             |
| E162 | [Plan a Minimal Incremental Rebuild](../content/problems/e162-plan-a-minimal-incremental-rebuild/lesson.json)                     | intermediate |    10 | E152, E153    |
