# The 200-lesson curriculum

This expansion adds 119 distinct lessons to the previous 81. The catalog now contains 200 lessons and one project checkpoint, with 2,244 public cases (1,246 new cases). The three guided paths contain 59 mathematics/ML, 79 deep-learning, and 62 AI-engineering lessons. Four interactive experiments and the retrieval project remain connected to the lesson library.

Every addition contains a learning task, explicit input and output conventions, three worked examples, progressive hints, an explanation, incomplete starter code, an inspectable reference, and an executable evaluator. Public cases test valid behavior as well as invalid inputs and input preservation. The catalog does not count framework ports, renamed questions, or number-swapped examples as extra lessons.

## Source use

Seven additions (D41–D47) adapt MIT-licensed Pyre-Code operations at commit `7ede95b47437798c74023a0ffae8fb33bbeebc2e`. [Their provenance](../content/deep200-provenance.json) retains source hashes, adaptation boundaries, and full upstream notices. The other 112 additions use original implementations, prose, and fixtures, with conceptual readings recorded in their package metadata. A conceptual reading is not a claim that its code or exercise text was imported.

The complete [119-item inventory](../content/curriculum-200-inventory.json) records objectives, prerequisites, cases, and attribution. Existing adaptation records remain separate, bringing actual Pyre-Code adaptations to 37.

## Verification approach

The native gate executes references, rejects incomplete starters and trivial answers, and checks sample counts. Independent suites exercise analytical identities, numerical derivatives, exhaustive small state spaces, probability conservation, and data-boundary invariants. Cross-batch checks ensure worked examples are the executed samples and reject canned example answers on valid inputs. Each published reference also runs in the isolated browser evaluator; exact executed results are recorded in [verification](verification.md).

The 2,000-activity curriculum is still the longer-term target. This release establishes 200 coding lessons; it does not claim a completed 2,000-item platform or a production account service.

## Mathematics and machine learning

40 additions: probability, statistical inference, matrix decompositions, classical models, clustering, kernels, and quantile estimation.

| ID  | Learning objective                                                                                                      | Public cases | Helpful first |
| --- | ----------------------------------------------------------------------------------------------------------------------- | -----------: | ------------- |
| M20 | [Update Beliefs with Evidence](../content/problems/m20-bayesian-evidence-update/lesson.json)                            |           10 | —             |
| M21 | [Measure Categorical Uncertainty](../content/problems/m21-categorical-entropy/lesson.json)                              |           10 | —             |
| M22 | [Measure Distribution Mismatch](../content/problems/m22-relative-entropy/lesson.json)                                   |           10 | M21           |
| M23 | [Compare Distributions Symmetrically](../content/problems/m23-jensen-shannon-divergence/lesson.json)                    |           11 | M22           |
| M24 | [Find Dependence in a Joint Table](../content/problems/m24-joint-mutual-information/lesson.json)                        |           11 | M21, M22      |
| M25 | [Interpolate Empirical Quantiles](../content/problems/m25-linear-empirical-quantiles/lesson.json)                       |           10 | —             |
| M26 | [Separate Scale from Linear Association](../content/problems/m26-pearson-correlation/lesson.json)                       |           10 | M09           |
| M27 | [Compare Order with Tied Ranks](../content/problems/m27-spearman-average-ranks/lesson.json)                             |           10 | M26           |
| M28 | [Scale Features with Robust Statistics](../content/problems/m28-median-iqr-scaling/lesson.json)                         |           10 | M05, M25      |
| M29 | [Remove Correlation with Symmetric Whitening](../content/problems/m29-symmetric-covariance-whitening/lesson.json)       |           10 | M09           |
| M30 | [Compress a Matrix with Singular Values](../content/problems/m30-truncated-svd-reconstruction/lesson.json)              |           10 | M15           |
| M31 | [Solve Rank Deficiency with a Pseudoinverse](../content/problems/m31-svd-pseudoinverse/lesson.json)                     |           11 | M30           |
| M32 | [Track a Dominant Matrix Direction](../content/problems/m32-power-iteration-rayleigh/lesson.json)                       |           10 | —             |
| M33 | [Build an Orthonormal Basis](../content/problems/m33-modified-gram-schmidt/lesson.json)                                 |           10 | —             |
| M34 | [Factor a Positive Definite Matrix](../content/problems/m34-cholesky-factorization/lesson.json)                         |           10 | —             |
| M35 | [Solve a Triangular System in Order](../content/problems/m35-forward-triangular-solve/lesson.json)                      |           11 | M34           |
| M36 | [Differentiate a Logistic Model](../content/problems/m36-logistic-regression-gradient/lesson.json)                      |           10 | M03, M04      |
| M37 | [Create Sparsity with a Proximal Step](../content/problems/m37-l1-proximal-threshold/lesson.json)                       |           10 | —             |
| M38 | [Follow Mistakes through a Perceptron Pass](../content/problems/m38-ordered-perceptron-pass/lesson.json)                |           10 | —             |
| M39 | [Differentiate the Margin Penalty](../content/problems/m39-hinge-loss-subgradient/lesson.json)                          |           10 | M38           |
| M40 | [Choose a Gini Decision Split](../content/problems/m40-gini-decision-stump/lesson.json)                                 |           11 | —             |
| M41 | [Move Cluster Centers to Their Assigned Means](../content/problems/m41-centroid-reestimation/lesson.json)               |           10 | M14           |
| M42 | [Diagnose Cluster Separation](../content/problems/m42-silhouette-diagnostics/lesson.json)                               |           10 | M12, M14      |
| M43 | [Identify Density-Based Core Points](../content/problems/m43-density-core-neighborhoods/lesson.json)                    |           11 | M12           |
| M44 | [Refine a Gaussian Mixture with Soft Assignments](../content/problems/m44-gaussian-mixture-em-step/lesson.json)         |           10 | M16, M20      |
| M45 | [Merge the Nearest Clusters](../content/problems/m45-single-linkage-merge/lesson.json)                                  |           10 | M12           |
| M46 | [Learn a Count-Based Class Model](../content/problems/m46-multinomial-naive-bayes-fit/lesson.json)                      |           10 | M16           |
| M47 | [Read Probability from an Empirical CDF](../content/problems/m47-empirical-cumulative-distribution/lesson.json)         |           10 | M25           |
| M48 | [Audit Supplied Bootstrap Resamples](../content/problems/m48-bootstrap-resample-means/lesson.json)                      |           10 | —             |
| M49 | [Compare Means under Relabeled Groups](../content/problems/m49-permutation-mean-test/lesson.json)                       |           10 | —             |
| M50 | [Standardize Paired Differences](../content/problems/m50-paired-t-statistic/lesson.json)                                |           10 | —             |
| M51 | [Evaluate Binomial Evidence in Log Space](../content/problems/m51-binomial-log-likelihood/lesson.json)                  |           10 | —             |
| M52 | [Update a Beta Belief about a Rate](../content/problems/m52-beta-binomial-update/lesson.json)                           |           10 | M20, M51      |
| M53 | [Score a Sequence while Updating Category Beliefs](../content/problems/m53-categorical-predictive-sequence/lesson.json) |           10 | M52           |
| M54 | [Measure Distance in Covariance Geometry](../content/problems/m54-mahalanobis-distance/lesson.json)                     |           10 | M09, M29      |
| M55 | [Measure the Cost of Moving Probability Mass](../content/problems/m55-empirical-wasserstein-distance/lesson.json)       |           10 | M47           |
| M56 | [Turn Distances into Radial Similarities](../content/problems/m56-rbf-kernel-matrix/lesson.json)                        |           10 | M12           |
| M57 | [Center Features through Their Kernel](../content/problems/m57-kernel-double-centering/lesson.json)                     |           10 | M56           |
| M58 | [Fit a Monotone Sequence](../content/problems/m58-weighted-isotonic-regression/lesson.json)                             |           10 | —             |
| M59 | [Train for an Asymmetric Quantile](../content/problems/m59-pinball-quantile-loss/lesson.json)                           |           10 | M25, M39      |

## Deep learning and reinforcement learning

39 additions: recurrent networks, backward passes, graph and attention operations, structured sequence models, generative objectives, rollout estimators, and policy/value updates.

| ID  | Learning objective                                                                                                        | Public cases | Helpful first |
| --- | ------------------------------------------------------------------------------------------------------------------------- | -----------: | ------------- |
| D41 | [Control a Normalized Branch with a Gate](../content/problems/d41-conditional-normalization-gate/lesson.json)             |           11 | D03           |
| D42 | [Share Key and Value Heads across Query Groups](../content/problems/d42-grouped-query-heads/lesson.json)                  |           11 | D04           |
| D43 | [Subtract Two Attention Maps](../content/problems/d43-differential-attention/lesson.json)                                 |           11 | D04           |
| D44 | [Learn a Mixture over Graph Neighbors](../content/problems/d44-graph-attention-neighbors/lesson.json)                     |           11 | D28           |
| D45 | [Build Messages from Nodes and Edge Features](../content/problems/d45-edge-conditioned-messages/lesson.json)              |           11 | D29           |
| D46 | [Advance a Diagonal State-Space Memory](../content/problems/d46-selective-state-space-step/lesson.json)                   |           11 | D02           |
| D47 | [Recombine a Feedforward Layer from Shards](../content/problems/d47-sharded-mlp-reduction/lesson.json)                    |           11 | D23           |
| D48 | [Carry a Hidden State through a Sequence](../content/problems/d48-vanilla-recurrent-state/lesson.json)                    |           11 | D02, D08      |
| D49 | [Separate LSTM Cell Memory from Hidden Output](../content/problems/d49-lstm-memory-gates/lesson.json)                     |           11 | D08, D48      |
| D50 | [Distinguish GRU Reset from Update Gates](../content/problems/d50-gru-reset-and-update/lesson.json)                       |           11 | D08, D48      |
| D51 | [Keep the Identity Path during Backpropagation](../content/problems/d51-residual-branch-backward/lesson.json)             |           11 | D02, D05      |
| D52 | [Distribute Average-Pooling Gradients](../content/problems/d52-average-pool-adjoint/lesson.json)                          |           12 | D10           |
| D53 | [Differentiate a Spatial Cross-Correlation](../content/problems/d53-convolution-backward/lesson.json)                     |           11 | D09, D02      |
| D54 | [Construct a Transposed Convolution by Scattering](../content/problems/d54-transposed-convolution-scatter/lesson.json)    |           12 | D09, D53      |
| D55 | [Normalize Channels in Separate Groups](../content/problems/d55-group-normalization/lesson.json)                          |           11 | D03, D25      |
| D56 | [Sum the Probability of CTC Alignments](../content/problems/d56-ctc-alignment-likelihood/lesson.json)                     |           11 | D02           |
| D57 | [Measure a Latent Gaussian against a Unit Prior](../content/problems/d57-diagonal-gaussian-kl/lesson.json)                |           11 | M08           |
| D58 | [Differentiate through a Supplied Noise Draw](../content/problems/d58-reparameterization-backward/lesson.json)            |           11 | D57, D02      |
| D59 | [Recover the Conditional Diffusion Posterior](../content/problems/d59-diffusion-posterior/lesson.json)                    |           11 | D32           |
| D60 | [Separate Discriminator and Generator Objectives](../content/problems/d60-logistic-adversarial-loss/lesson.json)          |           11 | M04           |
| D61 | [Compare Positive and Negative Embedding Distances](../content/problems/d61-triplet-margin-geometry/lesson.json)          |           11 | M12           |
| D62 | [Average Log Probabilities across Positive Partners](../content/problems/d62-multi-positive-contrastive-loss/lesson.json) |           12 | D27           |
| D63 | [Measure Soft Segmentation Overlap](../content/problems/d63-soft-dice-overlap/lesson.json)                                |           11 | M04           |
| D64 | [Differentiate an Image Smoothness Penalty](../content/problems/d64-total-variation-gradient/lesson.json)                 |           11 | D01           |
| D65 | [Apply a Softmax Jacobian without Building It](../content/problems/d65-softmax-jacobian-vector/lesson.json)               |           11 | M02, D02      |
| D66 | [Estimate a Matrix Trace with Sign Probes](../content/problems/d66-hutchinson-trace-probes/lesson.json)                   |           11 | D01           |
| D67 | [Trace Gradients through Attention Scores and Values](../content/problems/d67-attention-backward/lesson.json)             |           11 | D04, D65      |
| D68 | [Normalize Scores over Every Label Sequence](../content/problems/d68-chain-log-partition/lesson.json)                     |           11 | M02           |
| D69 | [Recover the Best Label Sequence with Backtracking](../content/problems/d69-chain-viterbi-path/lesson.json)               |           11 | D68           |
| D70 | [Trace Returns across Episode Boundaries](../content/problems/d70-discounted-episode-returns/lesson.json)                 |           11 | M08           |
| D71 | [Combine Temporal-Difference Residuals with GAE](../content/problems/d71-generalized-advantage-estimation/lesson.json)    |           13 | D70           |
| D72 | [Separate Value Targets from Current Predictions](../content/problems/d72-one-step-value-targets/lesson.json)             |           11 | D70           |
| D73 | [Separate Action Selection from Action Evaluation](../content/problems/d73-double-q-target-selection/lesson.json)         |           11 | D72           |
| D74 | [Project a Distributional Value Target](../content/problems/d74-categorical-value-projection/lesson.json)                 |           12 | D72           |
| D75 | [Turn Uniform Draws into a Categorical Choice](../content/problems/d75-gumbel-max-sampling/lesson.json)                   |           12 | M02           |
| D76 | [Differentiate a Categorical Policy Objective](../content/problems/d76-categorical-policy-score-gradient/lesson.json)     |           11 | M04, D70      |
| D77 | [Move a Target Network Gradually](../content/problems/d77-polyak-target-update/lesson.json)                               |           11 | D72           |
| D78 | [Inspect Potential-Based Reward Shaping](../content/problems/d78-potential-reward-shaping/lesson.json)                    |           11 | D70           |
| D79 | [Stop an N-Step Target at the Right Boundary](../content/problems/d79-n-step-bootstrap-targets/lesson.json)               |           11 | D70, D72      |

## AI engineering

40 additions: text metrics, retrieval, evaluation boundaries, calibration, data structures, streaming state, decoding, and inference operations.

| ID  | Learning objective                                                                                                   | Public cases | Helpful first |
| --- | -------------------------------------------------------------------------------------------------------------------- | -----------: | ------------- |
| E23 | [Count Overlapping Token N-grams](../content/problems/e23-token-ngram-counts/lesson.json)                            |           10 | —             |
| E24 | [Compare Repeated Terms with Multiset Jaccard](../content/problems/e24-multiset-jaccard/lesson.json)                 |           10 | E23           |
| E25 | [Measure Token Edit Distance](../content/problems/e25-token-edit-distance/lesson.json)                               |           10 | —             |
| E26 | [Inspect ROUGE-L Precision and Recall](../content/problems/e26-rouge-l-score/lesson.json)                            |           10 | E25           |
| E27 | [Explore Clipping and Brevity in BLEU-1](../content/problems/e27-clipped-unigram-bleu/lesson.json)                   |           10 | E23           |
| E28 | [Build a Positional Posting Index](../content/problems/e28-term-posting-index/lesson.json)                           |           10 | E23           |
| E29 | [Intersect and Exclude Posting Lists](../content/problems/e29-boolean-posting-query/lesson.json)                     |           10 | E28           |
| E30 | [Keep Related Rows in One Split](../content/problems/e30-group-heldout-split/lesson.json)                            |           10 | —             |
| E31 | [Split Time-Ordered Data with an Embargo](../content/problems/e31-chronological-embargo-split/lesson.json)           |           10 | —             |
| E32 | [Fit Median Imputation on Training Rows](../content/problems/e32-training-median-imputation/lesson.json)             |           10 | —             |
| E33 | [Audit Missingness Patterns](../content/problems/e33-missingness-pattern-audit/lesson.json)                          |           10 | E32           |
| E34 | [Measure Binned Population Shift](../content/problems/e34-population-stability-index/lesson.json)                    |           10 | —             |
| E35 | [Compare Empirical Distributions with KS Distance](../content/problems/e35-empirical-ks-distance/lesson.json)        |           11 | —             |
| E36 | [Construct Split-Conformal Intervals](../content/problems/e36-split-conformal-interval/lesson.json)                  |           10 | —             |
| E37 | [Audit Interval Coverage and Width](../content/problems/e37-prediction-interval-audit/lesson.json)                   |           10 | E36           |
| E38 | [Compare Paired Outcomes with an Exact Sign Test](../content/problems/e38-paired-sign-test/lesson.json)              |           10 | —             |
| E39 | [Choose Predictions by Expected Error Cost](../content/problems/e39-cost-sensitive-decisions/lesson.json)            |           10 | E16           |
| E40 | [Compare Error Rates Across Groups](../content/problems/e40-group-error-rate-audit/lesson.json)                      |           10 | E14           |
| E41 | [Trace Precision and Recall at Tied Scores](../content/problems/e41-precision-recall-operating-points/lesson.json)   |           10 | E14           |
| E42 | [Compare Boxes with Intersection over Union](../content/problems/e42-box-intersection-over-union/lesson.json)        |           10 | —             |
| E43 | [Suppress Redundant Detection Boxes](../content/problems/e43-greedy-box-suppression/lesson.json)                     |           10 | E42           |
| E44 | [Encode Consecutive Runs](../content/problems/e44-run-length-segments/lesson.json)                                   |           10 | —             |
| E45 | [Quantize with an Affine Zero Point](../content/problems/e45-affine-int8-quantization/lesson.json)                   |           11 | E18           |
| E46 | [Reconstruct Logical Tokens from KV Pages](../content/problems/e46-paged-kv-gather/lesson.json)                      |           10 | E19           |
| E47 | [Explore Beam Search on a Transition Table](../content/problems/e47-table-beam-search/lesson.json)                   |           10 | —             |
| E48 | [Verify Draft Tokens and Correct a Rejection](../content/problems/e48-speculative-token-verification/lesson.json)    |           11 | E20           |
| E49 | [Accumulate Unequal Microbatch Gradients](../content/problems/e49-sample-weighted-gradient-accumulation/lesson.json) |           10 | —             |
| E50 | [Unscale Gradients and Skip Overflowed Steps](../content/problems/e50-gradient-loss-unscaling/lesson.json)           |           10 | —             |
| E51 | [Sample a Stream with a Fixed-Size Reservoir](../content/problems/e51-reservoir-sampling-trace/lesson.json)          |           10 | —             |
| E52 | [Update Running Mean and Variance State](../content/problems/e52-welford-stream-update/lesson.json)                  |           11 | —             |
| E53 | [Merge Statistics from Separate Partitions](../content/problems/e53-parallel-moment-merge/lesson.json)               |           10 | E52           |
| E54 | [Select Weighted Samples with Exponential Keys](../content/problems/e54-weighted-reservoir-priorities/lesson.json)   |           10 | E51           |
| E55 | [Map Tokens into a Fixed Feature Space](../content/problems/e55-signed-feature-hashing/lesson.json)                  |           10 | E23           |
| E56 | [Estimate Frequencies with a Count-Min Sketch](../content/problems/e56-count-min-sketch/lesson.json)                 |           10 | E55           |
| E57 | [Inspect Bloom Filter False Positives](../content/problems/e57-bloom-membership-filter/lesson.json)                  |           10 | E55           |
| E58 | [Trace Least-Recently-Used Eviction](../content/problems/e58-lru-cache-trace/lesson.json)                            |           10 | —             |
| E59 | [Simulate Token-Bucket Admission](../content/problems/e59-token-bucket-admission/lesson.json)                        |           10 | —             |
| E60 | [Pack Consecutive Sequences Under a Padding Budget](../content/problems/e60-padding-budget-batches/lesson.json)      |           10 | E10           |
| E61 | [Interleave Two Rankings Without Duplicates](../content/problems/e61-alternating-ranking-interleave/lesson.json)     |           10 | E02           |
| E62 | [Join Only Features Available at Prediction Time](../content/problems/e62-causal-asof-feature-join/lesson.json)      |           10 | E31           |
