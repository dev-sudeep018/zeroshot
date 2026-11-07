# Milestones

## Completed foundation

The first isolated Python workspace and open-source repository foundation are merged in PR #1. GitHub Actions validates content, code quality, builds, and Chromium/Firefox/WebKit behavior. The protected main branch requires all four checks.

## Connected learning release

The working branch adds twelve original lessons, three guided paths, four interactive experiments, a retrieval project and Python integration checkpoint, per-lesson drafts, local progress, and backup import/export. The runner resolves explicit versioned content from a generated manifest. See verification.md for the exact checks and limitations.

## Continuing work

The [450-question expansion](curriculum-450.md) adds 250 distinct activities, including 195 beginner lessons. There are now 450 lessons plus one project checkpoint, with 4,760 public cases. The three full paths contain 159, 129, 162 lessons. A curated beginner route and beginner library entry reuse these lessons and their progress. Two existing lessons are debugging investigations. The interface retains semantic feedback and syntax colors on black/grey surfaces. Full verification is recorded in verification.md.

The [platform pilot](platform-pilot.md) adapts Pyre-Code exercises for RMSNorm,
RoPE, LoRA, cosine scheduling, focal loss and INT8 quantization. Source revisions,
hashes and upstream MIT notices are preserved. TensorTonic and Deep-ML remain
external references under their inspected terms.

The [second platform batch](platform-batch-02.md) adds twelve lessons on smooth
activations, gated projections, training statistics, target distributions,
contrastive learning, graph aggregation/readout, image patches, diffusion schedules,
cached causal attention and decoding distributions. Independent tests check
mathematical properties and plausible misconceptions for all twelve.

The [third platform batch](platform-batch-03.md) adds twelve distinct objectives
on policy and preference losses, flow and diffusion, attention variants, graph
reconstruction, separable convolution and expert routing. It adds 144 public cases
and keeps the source revision, notices and adaptation boundaries explicit.

The retrieval project now connects the document-term, BM25 and context-budget
lessons to inspectable scores and evidence selection. Its version 2 report
includes all source data and selection decisions. This is a deeper project flow,
not an increase in the lesson count; see retrieval-project.md.

1. Expand the authored curriculum toward 2,000 problems across the topic map in curriculum.md. Review distinct learning objectives; do not count number-swapped variants as new material.
2. Extend learning formats with debugging investigations, research replication, and larger projects.
3. Add optional account synchronization with tested database authorization and explicit local/cloud merging. Anonymous learning remains complete without an account.
4. Add opt-in measurement only when there is a useful learning question; do not collect source code or raw private queries.
5. Configure production hosting and independently verify separate credential-free runner domains, headers, caches, and failure recovery.
6. Obtain independent mathematical/security review and real learner feedback, including screen-reader and physical mobile-device testing.

No production deployment, account synchronization, or 2,000-item completed curriculum is claimed by this release.
