# Foundation expansion: M20–M59

This batch adds 40 original, executable NumPy lessons. Each package includes three worked examples, progressive hints, a reference, an unfinished starter, an explanation, and 10–11 public cases. The batch has 406 public cases and 23 independent numerical/property test methods in `tests/python/test_math200.py`.

The packages are original ZeroShot work: prose under CC-BY-SA-4.0 and code under Apache-2.0. No platform exercise text, reference code, or tests were imported. Primary documentation checked for conceptual conventions is linked below and in the corresponding packages.

## Learning objectives

| IDs     | Topics                                                                                                                                                               |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| M20–M24 | Bayesian evidence, entropy, directed KL, Jensen–Shannon divergence, joint mutual information                                                                         |
| M25–M29 | Linear quantiles, Pearson correlation, tied-rank Spearman correlation, robust training-only scaling, regularized symmetric whitening                                 |
| M30–M35 | Truncated SVD, cutoff pseudoinverse, power iteration, modified Gram–Schmidt, Cholesky, triangular substitution                                                       |
| M36–M40 | Logistic gradients, L1 proximal optimization, ordered perceptron updates, hinge subgradients, weighted-Gini split selection                                          |
| M41–M46 | Centroid estimation, silhouette diagnostics, density neighborhoods, full univariate mixture EM step, single-linkage merge, multinomial NB fitting                    |
| M47–M53 | Empirical CDF, supplied bootstrap resamples, supplied permutation test, paired statistic, binomial count likelihood, Beta posterior, sequential Dirichlet prediction |
| M54–M59 | Mahalanobis geometry, empirical Wasserstein transport, RBF kernels, implicit feature centering, weighted isotonic regression, pinball quantile loss                  |

## Scope and numerical review

These activities teach distinct operations, with explicit conventions where several mathematically valid choices exist. The mixture lesson performs both soft assignment and parameter fitting. The Dirichlet lesson scores a changing predictive sequence. Density neighborhoods are explicitly a stage of clustering, not an implementation of full DBSCAN.

Independent checks cover reconstruction and orthogonality identities, finite-difference gradients, binomial normalization, posterior composition, EM likelihood improvement, exhaustive isotonic block partitions, scalar distance/statistic oracles, and transport invariances. Public regression fixtures cover subnormal probability support, tiny joint mass, finite-output limits in inverse/solve routines, representable split thresholds, and tiny nonzero neighborhood distances.

Native verification passed for all 40 references, starter rejection, sample alignment, trivial wrong-answer rejection, all 406 public cases, and all 23 independent methods. Browser execution is part of the parent catalog integration gate.

## Concept references

- [NumPy quantile conventions](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html)
- [scikit-learn Gaussian mixture overview](https://scikit-learn.org/stable/modules/mixture.html)
- [SciPy Wasserstein-1 definition](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wasserstein_distance.html)
- [scikit-learn isotonic regression specification](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.isotonic_regression.html)
