# Third licensed exercise-platform batch

Checked 24 October 2026. Twelve additional activities adapt distinct operations
from the pinned MIT-licensed Pyre-Code / TorchCode source. They add 144 public
cases, bringing the published catalog to 81 lessons plus one project checkpoint
and 998 public cases. The paths contain 19 mathematics/ML, 40 deep learning and
22 engineering lessons. Fork duplicates and numeric variants do not add to these
counts.

## Learning objectives and adaptation choices

| ID  | Learning question                                                | Scope and conventions                                                                     |
| --- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| M18 | How does advantage sign change PPO clipping?                     | Forward clipped surrogate; supplied log probabilities and advantages; no training loop    |
| M19 | How does a reference policy change a preference objective?       | Sequence-level DPO margin and stable softplus; no reward or language-model training       |
| D33 | What changes along a straight noise-to-data path?                | Interpolation, constant target velocity and elementwise mean squared error                |
| D34 | How does an estimated noise direction produce an earlier sample? | Deterministic eta-zero DDIM with cumulative retentions and an exposed clean estimate      |
| D35 | How does distance bias interact with content scores?             | Bidirectional ALiBi attention with supplied head slopes, not a generated slope schedule   |
| D36 | Which tokens can influence a local query?                        | Bidirectional radius windows, boundary normalization and local slices                     |
| D37 | What does channel factorization change?                          | Valid depthwise cross-correlation followed by pointwise channel mixing                    |
| D38 | What neighborhood information does a sum retain?                 | GIN sum aggregation, self coefficient and two-layer MLP with only hidden ReLU             |
| D39 | When can attention be reassociated?                              | ELU-plus-one kernel attention with additive epsilon; explicitly different from softmax    |
| D40 | What geometry does an edge decoder impose?                       | Inner-product sigmoid decoder only; supplied embeddings, symmetry and retained self-pairs |
| E21 | What do routing frequencies and probabilities measure?           | Top-one auxiliary loss with both distributions returned; one does not certify balance     |
| E22 | How are selected expert outputs combined?                        | Exact-k routing, deterministic ties and normalized mixtures of supplied expert vectors    |

Every activity has original teaching prose, three worked examples, progressive
hints, a starter, an attributed reference and twelve public cases. The lessons
join the existing paths and prerequisite graph. They inspect small numerical
operations; they do not claim to implement complete training or serving systems.

The upstream `gae.py` denotes a graph autoencoder, not generalized advantage
estimation. D40 adapts its decoder only and is classified accordingly.

## Sources and attribution

[The provenance manifest](../content/platform-batch-03-provenance.json) records
commit `7ede95b47437798c74023a0ffae8fb33bbeebc2e`, twelve source-file hashes, the
license hash and a per-item explanation of changes. Each package retains the full
MIT notice for duoan and kiren in both `THIRD_PARTY_NOTICE.md` and `solution.py`,
including the reference delivered to the browser. Original Python additions are
Apache-2.0 and original prose is CC BY-SA 4.0; upstream material retains MIT terms.
See the [pinned license](https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/LICENSE).

Only upstream source text was read; upstream programs, installers and tests were
not executed. Solution operations were ported to the existing NumPy runtime.
TensorTonic and Deep-ML remain link-only sources under the decisions recorded in
the [platform pilot](platform-pilot.md).

For broader algorithm context, see the original papers on
[PPO](https://arxiv.org/abs/1707.06347),
[DPO](https://arxiv.org/abs/2305.18290), and
[DDIM](https://arxiv.org/abs/2010.02502). The contracts above state the narrower
operations implemented here.

## Verification strategy

The content checker executes references, starters, sample cases and trivial wrong
answers. Fourteen added Python methods check independent scalar or dense-kernel
oracles, preference identities, flow derivatives, a synthetic diffusion
trajectory, locality, graph geometry, expert dispatch and retained notices.
Each public evaluator must reject a plausible conceptual mistake on valid input.
Examples include clipping every PPO ratio, normalizing gates before expert
selection, flipping a cross-correlation kernel and replacing an additive epsilon
with a denominator clamp.

Run `pnpm content:check m18 m19 d33 d34 d35 d36 d37 d38 d39 d40 e21 e22`, then
`pnpm check`. Browser tests discover the new references automatically.
[The verification record](verification.md) records executed checks and the
remaining device and learner-review limitations.
