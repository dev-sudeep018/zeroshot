# A connected curriculum of 2,000 learning problems

The target is 2,000 meaningful learning problems across twenty topic areas.
`content/curriculum-plan.json` records the target allocations. Those allocations
are a planning map, not 2,000 authored lessons. The application derives its
published count from validated content packages.

## Three ways into the same material

- Guided paths connect concepts, experiments, implementations, and reflection.
  Prerequisites explain useful connections without locking access.
- Projects start with a useful outcome. Learners inspect a dataset, build parts,
  compare behavior, and return to relevant lessons when they need an idea.
- The open lab starts with a question. Learners predict, change a variable, inspect
  a result, and move into the underlying implementation.

The library is discovery infrastructure, not a competition queue. No speed score,
global rank, acceptance-rate sorting, or streak pressure is part of this design.
Passing checks records practice history; it does not establish mastery by itself.

## Publication requirements

A new problem needs an original learning objective and a distinct reason to
exist. Changing numbers or renaming the same task does not earn another count.
Every published coding lesson contains:

1. An explanation of the idea and where it is useful.
2. An explicit input/output contract, assumptions, and edge conventions.
3. At least three worked examples and progressive hints.
4. Starter code, a reference, and public tests for normal and invalid inputs.
5. Prerequisites and a connection to a path or project.
6. A reference that passes in both native Python and the browser runtime.
7. Checks that reject incomplete and plausible incorrect implementations.
8. Original authorship or explicit licensing and attribution.

`validated` means automated validation passed. Maintainer review still assesses
the mathematics, teaching value, distinctness, and accessibility. Draft packages
are excluded from both the published catalog and the runner manifest. Published
lessons cannot depend on unpublished prerequisites.

## Scaling the implementation

The catalog carries metadata only. Static route generation reads a single lesson
package; each browser route receives that lesson's prose and code. The runner
loads only the selected versioned evaluator from a generated allowlist. Search
filters the metadata and renders at most 24 results at once.

IDs support more than two digits. A capacity test validates 2,000 distinct IDs
and a connected prerequisite graph. This is a structural test, not a claim that
2,000 complete lessons or their production build performance have been tested.

The current published set contains 81 lessons, four interactive experiments,
and one retrieval project with a Python integration checkpoint. Two lessons start
with explicitly flawed code for debugging investigations. See [the second batch](curriculum-depth.md)
for its nine objectives and [batch three](curriculum-batch-03.md) for thirty more,
including source provenance, explicit conventions, and verification strategy. The
[platform pilot](platform-pilot.md), [second platform batch](platform-batch-02.md),
and [third platform batch](platform-batch-03.md) add thirty licensed adaptations with their own learning contracts. Expanding the
topic coverage, adding debugging and replication formats, and reviewing each
new batch remain active work.

The [free-resource survey](source-research.md) identifies reusable teaching
material, linked courses, runtime constraints, and a faster batch workflow.
Sources and planned adaptations do not count as published lessons.
