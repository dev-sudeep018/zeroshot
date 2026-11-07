# ZeroShot: 2,000-lesson expansion plan

**Status: 450 validated lessons; 1,550 reserved additions. This plan publishes no new lessons.**

The requested deadline is 8 November 2026 at noon Asia/Kolkata. It does not waive quality gates or establish that unfinished work has passed review.

## Scope and sequencing

Reserve 540 mathematics lessons (m160–m699), 500 deep-learning lessons (d130–d629), and 510 engineering lessons (e163–e672), in 69 batches of 20 or 30. Each reservation remains uncounted until its concrete objective is reviewed against the catalog and other expansion objectives. Module scope items are work areas, not invented completed lessons.

The planning target is 946 substantive beginner additions, alongside the existing 205. Beginner means useful small-data and model operations, never print/syntax padding.

First authoring batch: m160–m179, numerical matrix structure and operators. Drafts remain in `work/curriculum2000/math01/`; shared catalog totals and paths are untouched.

## Existing-catalog audit

All 450 published titles and the first-batch neighboring objectives were inspected. Module exclusions record the nearest existing clusters. Highest overlap risks: normalization, attention variants, basic metrics, elementary record loops, scalar summaries and tokenizer wrappers. Changing a number, dataset, title, signature or normalizer does not establish distinction.

A candidate must introduce a different mathematical operation, state transition, constraint, representation, failure diagnosis or multi-step reasoning goal. Otherwise extend the existing lesson or link it as a prerequisite. A different application alone is insufficient.

## Release gates

1. Distinct objective and nearest-existing-lesson comparison before authoring
2. Original work or verified compatible license and complete attribution
3. Three worked examples, two progressive hints, stepwise explanation and at least ten meaningful public cases
4. Independent oracles use a different algorithm, derivation, enumeration or invariants
5. Explicit bounds, dtypes, shapes, ties, empty-input behavior and no mutation
6. Schema and prerequisite graph, native reference checks, starter failure and canned-answer rejection
7. Pinned Pyodide evaluation and browser execution/isolation checks
8. Editorial review and beginner/path integration before exact-count promotion
9. Production build, desktop/mobile QA and final GitHub CI before release claims

Materialized public fixtures are not independent correctness evidence. A separate suite must derive answers without using the reference implementation as its oracle. Test reference-fixture consistency as a distinct check.

## Bounded module reservations

### Mathematics and ML

#### M01: Matrix structure and numerical operators (m160–m179)

Inspect matrix structure and exploit it to build or solve small linear models.

Reservation: 20; beginner planning target: 10. Scope: matrix gains; symmetry; diagonal dominance; graph operators; sparse storage; structured solves.

Example: Solve boundary-constrained readings on a three-node sensor graph.

Overlap boundary: m33-m35 and m148-m149 already cover bases, Cholesky, triangular solves, Jacobi and pivoting.

#### M02: Discrete counting with constraints (m180–m199)

Count feasible assignments and weighted outcomes under finite restrictions.

Reservation: 20; beginner planning target: 12. Scope: forbidden pairs; occupancy caps; bounded compositions; rook placements; subset sums; counting automata.

Example: Count shift assignments with forbidden worker-task pairs.

Overlap boundary: m122 and m134-m139 cover hypergeometric counts, dice, combinations, inversions, grid routes, derangements and empty boxes.

#### M03: Measurement uncertainty and units (m200–m219)

Carry uncertainty and support through measurement calculations.

Reservation: 20; beginner planning target: 15. Scope: resolution intervals; covariance propagation; calibration residuals; instrument agreement; dimensional checks; censoring.

Example: Combine correlated sensor errors into the uncertainty of one estimate.

Overlap boundary: m60 calibration, m61 masked means, m08 weighted moments and m130 total variance are existing lessons.

#### M04: Interval and fixed-point arithmetic (m220–m239)

Compute conservative numerical bounds and explain representation error.

Reservation: 20; beginner planning target: 13. Scope: interval products; interval division; rounding envelopes; cancellation; saturation; error budgets.

Example: Bound a ratio when both readings have finite instrument resolution.

Overlap boundary: No re-skinned clipping, scalar arithmetic drills or library-wrapper exercises.

#### M05: Compositional data and allocations (m240–m259)

Reason about shares, constrained totals and comparisons.

Reservation: 20; beginner planning target: 12. Scope: closure; zero replacement; log-ratio transforms; balance coordinates; subcomposition; apportionment.

Example: Compare nutrient shares separately from total food quantity.

Overlap boundary: m65 conditional rows and m95 weight concentration are existing lessons.

#### M06: Circular and directional statistics (m260–m279)

Summarize measurements whose endpoints wrap around.

Reservation: 20; beginner planning target: 15. Scope: circular mean; resultant length; angular differences; wrapped intervals; phase unwrapping; directional dispersion.

Example: Summarize headings of 359 and 1 degrees correctly.

Overlap boundary: m106 polar coordinates is a prerequisite; changing angle units is not a new task.

#### M07: Survival and censoring (m280–m299)

Build empirical survival summaries without treating censoring as failure.

Reservation: 20; beginner planning target: 10. Scope: risk sets; Kaplan-Meier; Nelson-Aalen; censoring tables; restricted mean survival; tied events.

Example: Track failures and right-censoring in an equipment cohort.

Overlap boundary: m132 absorbing probabilities uses a different model; do not repeat forward transition tasks.

#### M08: Time-series decomposition and dependence (m300–m319)

Separate season, trend and residual dependence.

Reservation: 20; beginner planning target: 12. Scope: seasonal indices; detrending; partial autocorrelation; cross-correlation; change points; lag selection.

Example: Remove a weekly demand pattern and inspect residual lag dependence.

Overlap boundary: m72-m79 and m97-m99 cover basic smoothing, differences, interpolation, errors and rolling splits.

#### M09: Spectral representations (m320–m339)

Translate finite signals between time and frequency viewpoints.

Reservation: 20; beginner planning target: 10. Scope: DFT coefficients; phase; spectral leakage; windows; convolution theorem; frequency filters.

Example: Explain why a shifted sinusoid spreads across DFT bins.

Overlap boundary: Different frequencies or transform normalization conventions are not separate lessons.

#### M10: Constrained optimization (m340–m359)

Implement constraint-aware updates and verify feasibility.

Reservation: 20; beginner planning target: 8. Scope: simplex projection; active sets; KKT residuals; projected gradients; equality elimination; duality gaps.

Example: Allocate a budget across nonnegative weights under quadratic cost.

Overlap boundary: m37 proximal sparsity and m158 ridge coordinate minimization already exist.

#### M11: Uncertainty from small samples (m360–m379)

Compute uncertainty with explicit sampling assumptions.

Reservation: 20; beginner planning target: 11. Scope: studentized intervals; paired bootstrap; percentile bias; finite population correction; delta method; exact enumeration.

Example: Compare a paired bootstrap with one that breaks pairing.

Overlap boundary: m48-m50, m92 and m96 already cover basic resampling, paired differences, jackknife means and Wilson intervals.

#### M12: Causal estimands and adjustment (m380–m399)

Compute effects in supplied identifiable toy designs.

Reservation: 20; beginner planning target: 12. Scope: stratified adjustment; inverse propensity weights; overlap; difference-in-differences; standardization; instrumental ratios.

Example: Adjust a treatment comparison for unequal baseline-risk composition.

Overlap boundary: State causal assumptions; arithmetic alone does not establish identification.

#### M13: Experimental design and randomization (m400–m419)

Plan assignments that isolate comparisons.

Reservation: 20; beginner planning target: 14. Scope: blocked assignments; factorial contrasts; balance; paired assignment; allocation; crossover carryover.

Example: Balance treatments within blocks and compute an interaction contrast.

Overlap boundary: m17 stratified splits and e30 grouped splits are not new treatment-design lessons.

#### M14: Forecast reconciliation and scoring (m420–m439)

Make related forecasts obey constraints and evaluate distributions.

Reservation: 20; beginner planning target: 12. Scope: hierarchy matrices; reconciliation; quantile crossing; pinball aggregates; interval scores; coherence.

Example: Reconcile regional forecasts to a national total.

Overlap boundary: m59 quantile training, m97-m98 errors and e37 coverage are existing prerequisites.

#### M15: Risk and tail decisions (m440–m459)

Measure tails under explicit payoff models.

Reservation: 20; beginner planning target: 13. Scope: value at risk; expected shortfall; drawdown; stress scenarios; risk mixtures; downside deviation.

Example: Average the worst tenth of a discrete loss distribution with fractional tail mass.

Overlap boundary: m25 quantile interpolation alone is not a new risk lesson.

#### M16: Queueing and renewal models (m460–m479)

Translate arrival and service assumptions into performance calculations.

Reservation: 20; beginner planning target: 11. Scope: birth-death equilibrium; utilization; renewal counts; Little law; blocking; busy periods.

Example: Compare capacities using a finite-state queue and its blocking probability.

Overlap boundary: e149 and e151 already teach deterministic queue simulation and makespan.

#### M17: Stochastic process inference (m480–m499)

Infer finite process dynamics from observed transitions.

Reservation: 20; beginner planning target: 10. Scope: transition estimates; detailed balance; hitting times; stationary distributions; reversibility; entropy rate.

Example: Estimate route transitions and calculate their stationary distribution.

Overlap boundary: m131-m132 forward transitions and survival are excluded.

#### M18: Graph probability and diffusion (m500–m519)

Use graph structure to model flows and uncertainty.

Reservation: 20; beginner planning target: 9. Scope: random walks; commute time; diffusion kernels; harmonic measures; PageRank; cuts.

Example: Compare long-run visits with degrees and teleportation probabilities.

Overlap boundary: First math batch owns Laplacian construction and Dirichlet solves; existing graph neural layers are deep-learning operations.

#### M19: Three-dimensional geometry (m520–m539)

Recover geometric relationships and coordinate changes.

Reservation: 20; beginner planning target: 12. Scope: rigid transforms; cameras; plane intersections; ray tests; triangulation; alignment.

Example: Project points into a pinhole camera and flag those behind it.

Overlap boundary: m100-m119 already cover planar geometry, axes and plane construction.

#### M20: Spatial statistics and interpolation (m540–m559)

Measure spatial dependence under explicit neighborhood models.

Reservation: 20; beginner planning target: 10. Scope: variograms; Moran statistic; spatial weights; inverse-distance interpolation; radial bases; spatial validation.

Example: Compare spatial autocorrelation before and after trend removal.

Overlap boundary: m56 radial kernels and m79 linear interpolation remain prerequisites.

#### M21: Numerical calculus and differential models (m560–m579)

Audit discretizations and numerical error behavior.

Reservation: 20; beginner planning target: 8. Scope: adaptive quadrature; finite-volume flux; Runge-Kutta; stiffness; extrapolation; boundary conditions.

Example: Compare Euler and midpoint errors under step refinement.

Overlap boundary: m140-m149 already cover elementary polynomial calculus, roots, Simpson and Euler cooling.

#### M22: Monte Carlo with supplied draws (m580–m599)

Transform fixed randomness and diagnose estimator efficiency.

Reservation: 20; beginner planning target: 12. Scope: importance sampling; antithetic pairs; control variates; rejection; stratification; discrepancy.

Example: Compare a paired-uniform integral estimator with ordinary sampling.

Overlap boundary: m125 categorical inverse CDF and e51/e54 reservoir and weighted samples are excluded.

#### M23: Regression diagnostics and influence (m600–m619)

Explain sensitivity and misspecification in fitted models.

Reservation: 20; beginner planning target: 10. Scope: leverage; studentized residuals; Cook distance; leave-one-out updates; heteroscedasticity; collinearity.

Example: Find a low-residual observation whose removal changes the fit.

Overlap boundary: m151 simple-line fitting and m152 baseline comparison are existing lessons.

#### M24: Bayesian model checks (m620–m639)

Update and compare Bayesian models with explicit priors.

Reservation: 20; beginner planning target: 10. Scope: normal conjugacy; predictive mixtures; evidence ratios; grid posterior; credible regions; prior sensitivity.

Example: Update a finite parameter grid and predict a future noisy reading.

Overlap boundary: m20, m52 and m53 already teach Bayes rule and beta/category updates.

#### M25: Information and coding (m640–m659)

Connect probability to compression and dependence.

Reservation: 20; beginner planning target: 10. Scope: Huffman lengths; code validity; conditional information; channel capacity; redundancy; information gain.

Example: Compare prefix-code expected length with entropy.

Overlap boundary: m21-m24 entropy and divergences are prerequisites, not new formula wrappers.

#### M26: Transport and matching (m660–m679)

Recover cost-aware correspondences and mass movement.

Reservation: 20; beginner planning target: 8. Scope: transport plans; Sinkhorn scaling; assignment; slack mass; barycenters; dual feasibility.

Example: Move mass between bins while preserving both marginals.

Overlap boundary: m55 one-dimensional Wasserstein distance already exists; require plan recovery or new constraints.

#### M27: Decision analysis and reliability (m680–m699)

Choose actions under uncertainty and reliability requirements.

Reservation: 20; beginner planning target: 14. Scope: decision trees; value of information; reliability blocks; fault trees; regret; robust choices.

Example: Determine whether an imperfect inspection changes a maintenance decision.

Overlap boundary: e39 expected classification cost and m120 event sets are existing lessons.

### Deep learning

#### D01: Tensor layouts and indexing contracts (d130–d149)

Transform tensors while preserving sample and feature meaning.

Reservation: 20; beginner planning target: 15. Scope: axis composition; ragged offsets; broadcast adjoints; named contractions; block layouts; mask alignment.

Example: Reassemble unequal sequence segments without mixing samples.

Overlap boundary: Existing patchification, subpixel shuffle, embedding gather and repeated-token scatter are excluded.

#### D02: Spatial operators and boundaries (d150–d169)

Build spatial transformations with explicit boundary behavior.

Reservation: 20; beginner planning target: 12. Scope: dilation sampling; separable filters; inverse layouts; padding adjoints; deformable sampling; antialiasing.

Example: Compare reflection and zero padding at an image edge.

Overlap boundary: d09-d11 and d37 already cover convolution, pooling shape and separable convolution.

#### D03: Spatial derivatives and reconstruction (d170–d189)

Trace local contributions back through image operations.

Reservation: 20; beginner planning target: 9. Scope: resize adjoints; crop adjoints; overlap-add; sampling derivatives; max ties; unfold adjoints.

Example: Scatter overlapping window gradients into their original pixels.

Overlap boundary: d52-d54 and d108/d112 cover basic pooling, convolution gradients, unfolding and unpooling.

#### D04: Normalization diagnostics and derivatives (d190–d209)

Understand how normalization changes dependence and gradients.

Reservation: 20; beginner planning target: 10. Scope: batchnorm derivatives; RMS adjoints; instance normalization; whitening; epsilon sensitivity; running-state fusion.

Example: Compare predictions when training batch composition changes.

Overlap boundary: d03/d18/d25/d55/d126 already cover forward normalization and folding.

#### D05: Embedding objectives and geometry (d210–d229)

Construct representation objectives and diagnose collapse.

Reservation: 20; beginner planning target: 9. Scope: triplet mining; proxy objectives; uniformity; alignment; angular margins; anisotropy.

Example: Separate hard-negative selection from the contrastive gradient.

Overlap boundary: d27/d61/d62 already cover basic contrastive and triplet objectives.

#### D06: Variable-length sequence processing (d230–d249)

Preserve sequence semantics through batching and state changes.

Reservation: 20; beginner planning target: 14. Scope: packed scans; segmented recurrence; forcing masks; prefix lengths; stream resets; length-aware pooling.

Example: Reset only the recurrent states of sequences that end.

Overlap boundary: d100-d104 and e10/e60 already cover next-token pairs and basic padding.

#### D07: Attention architecture and attribution (d250–d269)

Inspect attention under different context and representation constraints.

Reservation: 20; beginner planning target: 9. Scope: cross-attention; head pruning; key compression; rotary interpolation; relative buckets; cache masks.

Example: Compare full context with compressed keys under the same mask.

Overlap boundary: Existing masked, local, kernel, grouped and differential attention and RoPE are prerequisites.

#### D08: Optimizer state and schedules (d270–d289)

Implement optimizer state and constraint handling.

Reservation: 20; beginner planning target: 12. Scope: Adagrad; RMSprop; AdaDelta; trust ratios; restarts; parameter groups.

Example: Trace coordinate adaptation under sparse gradients.

Overlap boundary: d14/d15/d21/d83/d95-d98 already cover momentum, Adam, warmup, freezes and decay.

#### D09: Learning objectives and robust gradients (d290–d309)

Derive losses with different statistical targets.

Reservation: 20; beginner planning target: 11. Scope: Poisson likelihood; Cauchy loss; ordinal loss; ranking margins; asymmetry; distribution labels.

Example: Compare squared and bounded-influence gradients on an outlier.

Overlap boundary: Cross entropy, focal, Huber, quantile and elementary contrastive objectives already exist.

#### D10: Calibration and uncertainty decomposition (d310–d329)

Separate confidence, ambiguity and disagreement.

Reservation: 20; beginner planning target: 12. Scope: Dirichlet moments; ensemble disagreement; entropy decomposition; rejection; calibration fitting; selective loss.

Example: Compare ensembles with the same mean and different disagreement.

Overlap boundary: d88/d89/d125/d128 and e16/e17 cover margins, ensembles, distillation and temperature derivatives.

#### D11: Image augmentation contracts (d330–d349)

Transform pixels and supervision in the same coordinates.

Reservation: 20; beginner planning target: 15. Scope: box transforms; keypoints; visibility; intensity constraints; paired crop; inverses.

Example: Rotate image coordinates and carry bounding boxes with them.

Overlap boundary: d117-d120 already cover erase, CutMix, mixup and restoration.

#### D12: Detection and localization (d350–d369)

Build geometry and matching inside detection training.

Reservation: 20; beginner planning target: 10. Scope: anchor assignment; box encoding; generalized overlaps; target maps; bipartite matching; centerness.

Example: Assign valid anchors while retaining unmatched objects.

Overlap boundary: e42/e43 basic IoU and suppression and d115/d116 heatmap location are excluded.

#### D13: Dense prediction objectives (d370–d389)

Reason about dense labels and class imbalance.

Reservation: 20; beginner planning target: 11. Scope: boundary distance; class weights; Lovasz surrogate; focal Tversky; panoptic matching; ignore regions.

Example: Score segmentation without counting ignored pixels as background.

Overlap boundary: d63 Dice and d114 region boundaries are existing lessons.

#### D14: Video and motion tensors (d390–d409)

Preserve temporal geometry and evaluate motion.

Reservation: 20; beginner planning target: 13. Scope: flow warps; temporal sampling; motion masks; alignment; tube overlap; temporal consistency.

Example: Warp a frame and mark out-of-bounds pixels.

Overlap boundary: Adding a time axis alone is not a distinct objective.

#### D15: Audio representations and reconstruction (d410–d429)

Connect waveforms, spectral frames and model targets.

Reservation: 20; beginner planning target: 11. Scope: STFT framing; overlap-add; mel filters; log energy; spectral convergence; alignment.

Example: Reconstruct a waveform and inspect window coverage.

Overlap boundary: Math spectral modules own transform theory; this module owns model-facing contracts and losses.

#### D16: Graph learning beyond neighborhood averages (d430–d449)

Build graph operators under explicit structural assumptions.

Reservation: 20; beginner planning target: 9. Scope: edge attention; graph pooling; positions; relations; sampling correction; link negatives.

Example: Correct aggregation with known neighbor inclusion probabilities.

Overlap boundary: d28-d30/d38/d40/d44/d45 already cover basic graph architectures.

#### D17: State-space and long-memory operators (d450–d469)

Inspect recurrence, discretization and convolution equivalents.

Reservation: 20; beginner planning target: 8. Scope: zero-order hold; selective state; scan composition; complex poles; impulse response; stability.

Example: Check a chunked scan against sequential recurrence.

Overlap boundary: d46 and d107 cover diagonal memory and streaming convolution.

#### D18: Generative noise schedules and solvers (d470–d489)

Relate parameterizations and numerical sampling steps.

Reservation: 20; beginner planning target: 8. Scope: velocity prediction; score conversion; posterior variance; predictor-corrector; conditioning; schedule interpolation.

Example: Convert epsilon prediction into velocity at one noise level.

Overlap boundary: d32-d34/d59 cover basic schedules, flows and reverse steps.

#### D19: Latent-variable objectives (d490–d509)

Build bounds and structured latent calculations.

Reservation: 20; beginner planning target: 9. Scope: importance-weighted bounds; categorical reparameterization; collapse diagnostics; code usage; KL annealing; mixtures.

Example: Compare an ELBO with an importance-weighted bound.

Overlap boundary: d57/d58/d122 cover Gaussian KL, reparameterization and VQ gradients.

#### D20: Reinforcement learning estimators (d510–d529)

Construct estimators under episode and behavior-policy contracts.

Reservation: 20; beginner planning target: 8. Scope: V-trace; importance ratios; soft values; distributional quantiles; entropy penalties; eligibility traces.

Example: Correct an off-policy trajectory without crossing episode boundaries.

Overlap boundary: d70-d79 and m18 already cover common TD, GAE and clipped objectives.

#### D21: Model compression and efficiency (d530–d549)

Quantify error while changing model representation.

Reservation: 20; beginner planning target: 12. Scope: pruning masks; rank selection; quantization error; sparse kernels; distillation; activation clipping.

Example: Prune under a budget and report output error and retained energy.

Overlap boundary: e18/e45, d20 and d123 already teach basic quantization, LoRA and spectral constraints.

#### D22: Automatic differentiation building blocks (d550–d569)

Represent dependencies and differentiate compositions.

Reservation: 20; beginner planning target: 8. Scope: JVP; VJP; Hessian-vector products; implicit gradients; broadcast reduction; recomputation.

Example: Differentiate a solved system using an adjoint solve.

Overlap boundary: Existing local layer gradients are prerequisites; no supplied-derivative wrappers.

#### D23: Training dynamics and numerical failure (d570–d589)

Diagnose training failures before curves hide them.

Reservation: 20; beginner planning target: 14. Scope: gradient noise; sharpness; scaling; signal propagation; update alignment; branch recovery.

Example: Compare microbatch gradient directions at the same aggregate loss.

Overlap boundary: d84-d99 already cover scales, saturation, clipping, conflicts and directional curvature.

#### D24: Continual and multi-task learning (d590–d609)

Control interference across objectives and time.

Reservation: 20; beginner planning target: 11. Scope: EWC; replay weighting; gradient projection; balancing; forgetting metrics; adapter merges.

Example: Measure backward transfer without confusing it with final average accuracy.

Overlap boundary: d93 conflict diagnosis alone is not a new learning operation.

#### D25: Interpretability and explanation checks (d610–d629)

Construct explanations and test their limits.

Reservation: 20; beginner planning target: 12. Scope: integrated gradients; occlusion; Shapley enumeration; counterfactuals; completeness; concepts.

Example: Compare attribution totals with a baseline-to-input output change.

Overlap boundary: d90/d91 linear contributions and input gradients already exist.

### AI engineering

#### E01: Relational records and reconciliation (e163–e192)

Preserve multiplicity and missingness across record combinations.

Reservation: 30; beginner planning target: 22. Scope: outer joins; anti joins; range joins; changing dimensions; ledgers; referential actions.

Example: Join orders to fulfillments without duplicating totals.

Overlap boundary: e63-e102 cover basic record loops and grouping; do not rename them.

#### E02: Data contracts and schema evolution (e193–e222)

Validate nested contract changes and report precise errors.

Reservation: 30; beginner planning target: 24. Scope: nested validation; union schemas; migrations; compatibility; decimals; nullability.

Example: Check an old reader against a changed producer schema.

Overlap boundary: e98/e129-e137 basic tabular checks are prerequisites.

#### E03: Unicode and text boundaries (e223–e252)

Align text with bytes and normalized forms.

Reservation: 30; beginner planning target: 21. Scope: normalization maps; combining marks; scripts; grapheme limits; offsets; casefold collisions.

Example: Map normalized matches back to original text spans.

Overlap boundary: e103-e113 ASCII and UTF-8 basics are excluded.

#### E04: Tokenization and structured language data (e253–e282)

Build deterministic preprocessing under ambiguity.

Reservation: 30; beginner planning target: 20. Scope: WordPiece; unigram segmentation; alignment; templates; span merging; nested delimiters.

Example: Find minimum-cost segmentation in a finite vocabulary.

Overlap boundary: e11/e12 BPE merge and basic tokenizers already exist.

#### E05: Retrieval indexes and query execution (e283–e312)

Test query semantics independently of ranking scores.

Reservation: 30; beginner planning target: 18. Scope: proximity; skip indexes; WAND bounds; fields; expansion; deletion.

Example: Find gapped phrases while preserving document positions.

Overlap boundary: Existing TF-IDF, BM25, postings, fusion, MMR and top-k are prerequisites.

#### E06: Evidence assembly for grounded generation (e313–e342)

Build traceable context and citations.

Reservation: 30; beginner planning target: 23. Scope: citation alignment; source deduplication; budgets; coverage; conflicts; provenance spans.

Example: Fit passages into context while retaining source spans.

Overlap boundary: e01/e13/e107 basic chunks and budgets need a new provenance or conflict objective.

#### E07: Evaluation datasets and diagnostic slices (e343–e372)

Aggregate evaluations without denominator errors.

Reservation: 30; beginner planning target: 22. Scope: slices; abstention; paired comparisons; multilabel metrics; uncertainty bins; annotations.

Example: Report subgroup performance and support, including empty slices.

Overlap boundary: Existing classification, ranking and agreement metrics cannot be repeated.

#### E08: Event-time stream processing (e373–e402)

Reconcile out-of-order observations with explicit timing rules.

Reservation: 30; beginner planning target: 20. Scope: watermarks; corrections; window updates; interval joins; retractions; exactly-once state.

Example: Revise a window when a late event arrives before closure.

Overlap boundary: e101/e144/e145 already cover ordered merges, fixed windows and sessions.

#### E09: Cache consistency and incremental state (e403–e432)

Represent freshness across dependent data.

Reservation: 30; beginner planning target: 19. Scope: version vectors; write-through; read repair; invalidation generations; delta replay; snapshots.

Example: Invalidate entries whose declared source versions changed.

Overlap boundary: e58/e146/e160-e162 cover basic LRU, idempotency and rebuilds.

#### E10: Scheduling and dependency execution (e433–e462)

Plan under resource, fairness and dependency constraints.

Reservation: 30; beginner planning target: 21. Scope: critical paths; fair queues; backpressure; packing; preemption; deadlines.

Example: Schedule a DAG under bounded memory and explain idle intervals.

Overlap boundary: e79/e80/e149-e153 basic scheduling is excluded.

#### E11: Admission control and resilient requests (e463–e492)

Make overload and failure policies testable.

Reservation: 30; beginner planning target: 23. Scope: sliding windows; adaptive retries; hedging; jitter allocation; bulkheads; failure budgets.

Example: Compare burst admission under a sliding time limit.

Overlap boundary: e59/e147/e148 token bucket, retries and circuit breaker already exist.

#### E12: Model and tensor interchange (e493–e522)

Encode tensor dtype, order, alignment and integrity.

Reservation: 30; beginner planning target: 21. Scope: strides; endian conversion; bit packing; shard manifests; checksums; shape metadata.

Example: Reassemble shards and detect swapped axes or missing byte ranges.

Overlap boundary: e157-e159 byte frames and digests need new tensor structure.

#### E13: Feature pipelines and lineage (e523–e552)

Apply training transformations reproducibly to later data.

Reservation: 30; beginner planning target: 23. Scope: crosses; leakage audit; availability; bitemporal joins; category evolution; lineage.

Example: Recover feature values actually available at prediction time.

Overlap boundary: e32/e62/e136 already cover imputation, as-of joins and categories.

#### E14: Experiment tracking and reproducibility (e553–e582)

Make run comparisons and reruns trustworthy.

Reservation: 30; beginner planning target: 24. Scope: seed scope; configuration diffs; manifests; split fingerprints; paired runs; resumable trials.

Example: Detect experiments with different data versions or splits.

Overlap boundary: No exercises that merely stringify metadata or print a seed.

#### E15: API contracts and batch inference (e583–e612)

Align requests and responses under partial failures.

Reservation: 30; beginner planning target: 24. Scope: batch alignment; cursors; structured validation; deadlines; cancellation; error envelopes.

Example: Reorder asynchronous results while retaining per-item errors.

Overlap boundary: e81 and e116-e128 basic pagination and parsing are excluded.

#### E16: Privacy and input-boundary operations (e613–e642)

Implement bounded defensive handling under stated assumptions.

Reservation: 30; beginner planning target: 22. Scope: allowlists; masking; expansion limits; provenance filters; anonymized aggregates; policies.

Example: Redact data and report removed spans without logging secrets.

Overlap boundary: No production-security guarantee; e106/e126 basics are existing lessons.

#### E17: Serving resource and cost accounting (e643–e672)

Calculate resource plans from requests and model dimensions.

Reservation: 30; beginner planning target: 24. Scope: KV memory; padding waste; throughput; energy; batching latency; concurrency.

Example: Choose a batch that fits memory and report padding overhead.

Overlap boundary: Existing KV, expert routing, gradient accumulation and packing lessons remain prerequisites.

## Provenance and reuse

Free access is not a reuse license. Distinguish original work, conceptual references, and adapted code/text. Verify licenses before importing material. TrenTorch can inform product research without allowing its content to be copied into this curriculum.

The first matrix batch uses original code, prose and fixtures. Concept references include [NumPy matrix norms](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm), [Netlib Templates](https://www.netlib.org/templates/templates.html), and [Cornell Gershgorin notes](https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-10-22.html). No external prose or implementation is copied.

## Delivery accounting

Report reserved, objective-reviewed, authored, independently checked, Pyodide-checked, browser-checked and published counts separately. Publish coherent validated batches through Git and GitHub. Keep incomplete drafts outside `content/problems`; never substitute the target for a measured count.
