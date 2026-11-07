# Verification record

## Curriculum production workflow — 25 October 2026

The published catalog remains 81 lessons plus one project checkpoint. This change
removes repeated production work: one reusable draft packager, one workflow per
feature PR update, one tested build shared across all browser jobs, and two
independent browser workers. See [the production guide](content-production.md).

Local `pnpm check` passed types, lint, formatting, 26 Vitest tests, 65 Python test
methods, all 82 content packages and the 94-page export. Seven new tests cover
source/license tampering, draft output, public evaluator execution, existing-file
preservation, path traversal, malformed later entries, sample correspondence and
reading upstream snapshots without executing them.

Repackaging the existing twelve-lesson third platform batch produced twelve draft
packages with all 144 reference cases passing, three samples per package and
incomplete starters rejected. These copies remain outside the published catalog
and do not add to its count.

The same 26 Chromium/WebKit checks used for the previous batch passed with two
workers in 1.9 minutes, compared with the recorded 3.0 minutes at one worker.
That is roughly 37% less elapsed time for this local check, not a guaranteed
curriculum-authoring speedup. All 300 tests remain in the full browser suite.
GitHub PR checks record the result of downloading and testing the shared artifact
in each browser; no browser job builds a second copy.

The previous batch's eight GitHub checks all passed at `d560c46` (PR #18).
No product UI, lesson content or runner isolation boundary changed in this pass.

## Third platform batch — 24 October 2026

Twelve further licensed adaptations bring the catalog to 81 lessons plus one
project checkpoint, with 998 public cases. The paths contain 19 mathematics/ML,
40 deep learning and 22 engineering lessons. See
[the batch record](platform-batch-03.md) for the distinct objectives, changed
interfaces and source provenance.

Local `pnpm check` passed metadata/prerequisite validation for 82 packages, types,
lint, formatting, 26 Vitest tests, 58 Python test methods and the 94-page export.
The focused content check passed twelve references and 144 public cases, including
starter, sample-count and trivial-wrong-answer checks. Fourteen added Python
methods cover independent numerical oracles, geometric and objective identities,
a synthetic diffusion trajectory, locality, expert dispatch, twelve plausible
conceptual mistakes rejected on valid input, and retained upstream notices.

All twelve new references and the learning-entry-point, library-filter and
experiment navigation regression passed in both Chromium and WebKit:
26 browser checks. The full browser suite discovers 100 tests per engine,
300 total; GitHub checks record the complete-suite results at the tested commit.

Five desktop/mobile captures of the policy-objective and expert-mixture lessons
were inspected after the editor loaded. Examples, hints, solution credits and the
mobile reading/editing switch worked. No document overflow was measured at 320,
390 or 1440 pixels, and no page errors occurred in those checks. Twelve upstream
task hashes and the license hash matched the pinned snapshots. All twelve
generated browser references exactly matched their credited source files, and
the two inspected solution views retained the full MIT notices.

The preceding batch's eight GitHub push and pull-request checks all passed at
`652cfda` (PR #17), including complete Chromium, Firefox and WebKit suites.
The Windows Firefox, physical-device and learner-review limitations below remain.

## Second platform batch — 24 October 2026

Twelve further licensed adaptations bring the catalog to 69 lessons plus one
project checkpoint, with 854 public cases. The new material covers activations,
gates, BatchNorm state, label smoothing, contrastive learning, graph operations,
image patches, diffusion schedules, cached attention and decoding distributions.
See [the batch record](platform-batch-02.md) for exact conventions and source use.

Local `pnpm check` passed metadata/prerequisite validation for 70 packages, types,
lint, formatting, 26 Vitest tests, 44 Python test methods and the 82-page export.
The focused content command passed all twelve references and 144 public cases.
Thirteen new Python methods include independent scalar and pixel-loop oracles,
graph permutation/duplication checks, cached/full attention equivalence across
three chunkings, and twelve conceptual mistakes rejected on valid input.

After the general project-link wording change, the production build and 26 focused
browser checks passed: all twelve new references plus the learning-entry-point,
library-filter and experiment regression in both Chromium and WebKit.

Four desktop/mobile captures of BatchNorm and cached-attention lessons were
inspected. Description, hints and solution tabs worked; measurements found no
document overflow at 320, 390 or 1440 pixels and no page errors. Twelve upstream
task hashes and the license hash matched their pinned source snapshots. All
twelve generated browser references exactly matched their credited source files,
and both inspected solution views retained the full upstream notices.

The full suite discovers 88 tests per engine; the GitHub pull-request
checks record full-suite results at the tested commit. The Windows Firefox and
physical-device limitations below still apply.

The preceding platform pilot's GitHub quality and complete Chromium, Firefox and
WebKit checks all passed at `1e4288a` (PR #16).

## Licensed platform adaptations — 24 October 2026

Six Pyre-Code / TorchCode adaptations add RMS normalization, rotary embeddings,
LoRA, cosine scheduling, focal loss and per-channel INT8 weights. There are now
57 lessons plus one project checkpoint, with 710 public cases. The source
decisions and changed numerical conventions are recorded in
[the platform pilot](platform-pilot.md).

Local `pnpm check` passed metadata validation for 58 packages, types, lint,
formatting, 26 Vitest tests, 31 Python test methods and the 70-page production
export. The focused content command checked all six new references and 73 public
cases. Nine new Python methods cover independent numerical invariants, valid-input
misconceptions, oversized scalar rejection and retained notices. NumPy warnings from deliberate invalid inputs
and wrong implementations are expected; the reference checks passed.

A regression initially reproduced six `OverflowError` failures when very large
Python integer scalars were converted to float. The references now translate that
conversion failure to the promised `ValueError`; relevant public invalid-input
checks include the boundary.

All six references passed in Chromium and WebKit (12 browser checks). The learning
entry-point, library-filter and experiment navigation regression also passed in
both engines (two further checks). Desktop RoPE and mobile INT8 lesson captures
were inspected; description, hints and solution tabs worked. Measurements found
no document overflow at 320, 390 or 1440 pixels and no page errors in that check.

SHA-256 checks matched the six pinned upstream task files and their license.
All six generated browser reference payloads exactly matched the credited source
files. Both inspected solution views displayed the complete MIT notices, including
the two upstream copyright holders. No upstream setup scripts or programs were
executed.

The complete browser suite discovers 76 tests per engine. GitHub pull-request
checks record full-suite results for the tested commit. The existing Windows
Firefox and physical-device limitations below still apply.

## Retrieval scores and evidence — 23 October 2026

The existing project now compares four retrieval methods, explains BM25 term
contributions, selects whole sources under a word budget, and exports a version 2
report containing its dataset and decisions. The catalog remains 51 lessons plus
one project checkpoint. See [the project guide](retrieval-project.md).

Local `pnpm check` passed metadata validation for 52 packages, types, lint,
formatting, 26 Vitest tests, 22 Python test methods, and the 64-page export.
After the final mobile-table guidance and focus treatment, the production build
and ten focused browser checks passed across Chromium and WebKit: six new checks
for scoring, selection, export and narrow layout, plus four existing project-note
and mobile-navigation regressions. The browser test initially imported a bundled
JSON module through Node without an import attribute; replacing that test-only
dependency with independent report assertions fixed test discovery.

Seven desktop/mobile captures were inspected. Measurements found no document
overflow at 320, 390, 768, 1100 or 1440 pixels and no page errors. The independent
finish reviewer returned `disposition: ship` with no material fixes. The extension
keeps the existing visual system. The detector's typography advisories are
recorded as incumbent design-record drift, not silently repaired.

The complete browser suite now discovers 70 tests per engine. GitHub checks on
the pull request record the tested revision and full-suite results. The Windows
Firefox and physical-device limitations below still apply.

## Thirty-activity curriculum batch — 23 October 2026

The third batch adds 30 distinct learning activities and 339 public cases. There
are now 51 lessons plus one project checkpoint, 637 public cases, and 17 lessons
per guided path. [The batch record](curriculum-batch-03.md) documents objectives,
conventions, source use, and verification scope.

Local `pnpm check` passed metadata/prerequisite validation for 52 packages,
TypeScript, ESLint, formatting, 16 Vitest tests, 22 Python test methods, and the
64-page production export. Ten new Python methods include independent numerical
properties, embedding finite differences, optimizer trajectories, source-notice
preservation, and 30 plausible misconceptions. Every misconception fails an
assertion on valid input. Intentional invalid starter/mutant executions can emit
NumPy warnings; these do not represent reference failures.

The browser suite discovers 67 tests per engine, including all 52 published
references. All 30 new references passed in local Chromium. The navigation test
initially used a phrase absent from the actual lesson title; its corrected search
passed on a focused rerun. Desktop BM25 content at 1440 pixels and mobile Gaussian
content at 390 pixels were inspected, with no document overflow or page errors.
Worked examples now display named inputs and numeric results instead of NumPy
constructor expressions. Metadata validation and the production build also cover
that presentation update. GitHub runs the complete suite in Chromium, Firefox, and
WebKit; the pull-request checks record the exact tested commit and results.
The existing Windows Firefox and physical-device limitations below still apply.

The D2L cross-correlation adaptation retains its upstream MIT-0 notice in both
the repository and browser-delivered reference. The other 29 activities have
original prose/code with concept references. The provenance manifest distinguishes
these cases. No additional runtime dependency, dataset, or external model service
was introduced. Source reuse and passing tests do not establish teaching quality;
independent review and learner feedback remain necessary.

The preceding batch's final GitHub quality, Chromium, Firefox, and WebKit checks
passed at `8a72bc41779d1e21d9f64f3e0f9ce5b1df2c3fc2`; PR #13 is ready for review.

## Curriculum depth, semantic colors, and source survey — 22 October 2026

That batch added nine distinct lessons, bringing the catalog to 21 lessons
plus one retrieval checkpoint and 298 public cases. Seven new Python test methods
check independent numerical properties and reject nine plausible conceptual
mistakes. They cover training-only scaling, ridge gradients, ReLU, dropout,
gradient clipping, retrieval representation, and ranking metrics.

Local validation, types, lint, formatting, 16 Vitest tests, 12 Python test
methods, and the 34-page production export pass. The browser suite has 37 tests per engine. The local Chromium/WebKit
run passed 72 of 74 initially; two Chromium cases encountered page-load or
closed-browser timeouts during the long run. Both passed on a focused rerun
(E07 and M01, 17.1 seconds combined). Subsequent completion-icon and confirmation
text CSS corrections were checked visually; the GitHub checks on the new commit
remain authoritative for the full release suite.

The fast `pnpm content:check` command checked the nine-package batch and 137 cases
in 2.8 seconds of native execution in the recorded run; this excludes metadata
loading/tool startup and is not a benchmark guarantee. An unknown ID returned
exit code 1. The full release command still executes every Python test, but no
longer executes the same suite twice. The batch command is a short feedback loop,
not a substitute for browser execution, numerical properties, or editorial review.

Semantic feedback uses green success, red failures, amber warnings/timeouts,
and blue information/cancellation. Python keywords, strings, and numbers have
separate syntax colors. Text and icons retain state meaning without hue. Checked
semantic text pairs exceed 6.8:1 against the brightest working surface (#272727);
syntax pairs exceed 7.8:1. These measurements are not a complete accessibility
audit. Desktop and mobile captures inspect actual failed/passed runs, replacement
warnings, stopped runs, syntax, and completion indicators. The first review attempt
hit a quota interruption and was replaced. The replacement reviewer found two
remaining neutral states: library completion and backup confirmation text. Both
were corrected and recaptured; the verdict scored both resolved with
`disposition: ship`, covering those fixes. The updated design records match the
final semantic roles. Review scope is also recorded on the pull request.

`images/semantic-workspace.jpg` is an original application capture showing a
previously completed softmax lesson's existing reference draft passing three
examples. It does not imply an example-only run grants completion. The earlier
screenshots and verification sections below record previous milestones.

The [resource survey](source-research.md) and `content/sources.json` record 21
inspected sources with license evidence and runtime assessments. No third-party
content was imported and no upstream program was executed. Sources, planned
adaptations, and linked courses do not count toward published lessons.

## Connected learning and monochrome palette — 21–22 October 2026

That earlier release connected three guided paths, four interactive experiments, a searchable lesson library, and a retrieval project. It contained 12 published lessons plus one Python integration checkpoint, with 161 public cases. The 2,000-item curriculum allocation is a target, not an authored-content count.

Local content validation, TypeScript, ESLint, formatting, 15 Vitest tests, five Python test methods, and the 25-page production export pass. Native validation checks every reference and rejects every incomplete starter and a trivial incorrect implementation. Independent numerical checks cover softmax shift invariance, finite-difference gradients, and attention masking.

The browser suite now contains 28 tests per engine. It covers all 13 published references, connected navigation, filters, experiment controls, retrieval metrics/report export, progress backup merges, preservation of existing drafts, cross-tab completion, mobile navigation, and the existing editor/isolation regressions. An additional manifest test verifies that unknown items and unsupported versions are rejected before execution. All 84 browser tests passed in the clean Linux runs for revision `500b672`; final per-engine results for later revisions are recorded on [pull request #12](https://github.com/dev-sudeep018/project-mastery/pull/12).

Local Chromium and WebKit runs covered the complete suite. Two backup-test assertions incorrectly read Monaco's input element instead of its rendered code; after correcting that test, all 14 focused checks passed across both engines, including backup import and cross-tab completion. The final editor palette adjustments were also inspected in the rendered browser.

The finish review inspected ten desktop/mobile captures and sampled the implementation. It found one missing accessibility state on the mobile reading/editor switch. The corrected buttons expose complementary pressed states, and the existing mobile flow test passes in local Chromium and WebKit. The reviewer scored that fix resolved with `disposition: ship`; this verdict covers the listed fix. The initial reviewer attempt was replaced after a quota interruption. The design records were rechecked after the correction and remain accurate. The final production export, focused lint, formatting, and type checks pass.

The black/light-grey palette uses shared CSS tokens in the site and Monaco editor. Measured text contrast is at least 5.58:1 for the checked subtle-text/hover pair; primary action text is 12.84:1. The strong control boundary has 3.48:1 contrast against the hover surface. Diagnostic labels and icons distinguish passed and failed states without hue. These checks are not a complete accessibility audit.

The 2,000-ID prerequisite-graph test validates metadata capacity only. It does not establish the build performance, editorial quality, or runtime load characteristics of 2,000 authored packages. No production account synchronization or public production deployment is included.

## Prior workspace milestone — 20 October 2026

The first workspace milestone is tracked in [pull request #1](https://github.com/dev-sudeep018/project-mastery/pull/1), now merged. The results below describe that earlier revision; the required GitHub checks are authoritative for each tested commit.

## Recorded local results

Environment: Windows, Node.js 24.13.0, pnpm 11.25.0, Python 3.14.5, NumPy 2.4.5, Playwright 1.64.1.

| Check                                                        | Result                                                                                  |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| Content schema, prerequisite graph, and reference validation | Passed for the one published exercise                                                   |
| TypeScript, ESLint, Prettier                                 | Passed                                                                                  |
| Vitest contracts and draft recovery                          | 8 tests passed                                                                          |
| Python evaluator and numerical properties                    | 3 tests passed                                                                          |
| Next.js production static export                             | Passed                                                                                  |
| Chromium browser and isolation suite                         | 10 tests passed                                                                         |
| WebKit browser and isolation suite                           | 10 tests passed                                                                         |
| Production dependency audit                                  | No known vulnerabilities reported at verification time                                  |
| Manual desktop/mobile review                                 | 1440 x 900 and 390 x 844 inspected; mobile replacement fix received `disposition: ship` |
| In-app browser console                                       | No errors reported in the final inspected preview                                       |

The reference implementation passes all 13 public exercise cases in both local Python and browser Python. The evaluator rejects incomplete and plausible incorrect solutions. Additional numerical checks cover invariance under adding a constant and preservation of the input.

Browser tests exercise starter failures, reference success, saved edits after reload, example-only runs, syntax errors, literal HTML output, cancellation, infinite-loop termination, fresh state between runs, navigation, search, keyboard tab/panel controls, and the mobile replacement prompt. Isolation probes check response CSP, blocked parent-document access, blocked application/external network requests from learner code, and rejection of forged or malformed messages.

## GitHub verification and maintenance

[GitHub Actions](https://github.com/dev-sudeep018/project-mastery/actions) performs clean Linux installs and runs four required jobs: content/types/lint/format/unit tests/build, plus one browser/isolation job for each of Chromium, Firefox, and WebKit. Use the checks on the pull request to inspect the precise tested commit and any retry. Failure artifacts retain screenshots and traces for seven days.

The `main` branch requires an up-to-date pull request with those four checks and resolved conversations, including for administrators. Force pushes and deletion are disabled. Private vulnerability reporting is enabled. Dependabot configuration is present on the default branch.

## Verification limits

The locally downloaded Firefox executable could not launch on this Windows host (`spawn UNKNOWN`), including after reinstalling the official Playwright binary. The GitHub Firefox job tests Linux independently; Windows Firefox is not claimed as verified.

Playwright WebKit is not a real Safari/iPhone device test. Mobile verification uses a narrow browser viewport. A full screen-reader review, actual mobile-device testing, production hosting/header verification, load testing, and an independent security audit remain future work. Browser workers do not provide a hard memory quota; completion is local, mutable practice feedback.

Automated editor replacement dispatches a synthetic paste payload through Monaco's DOM handler and verifies the saved code exactly. It covers editor changes and persistence, not operating-system clipboard permissions or integration.

The first milestone contained one complete exercise. The connected-learning release expands it to the counts recorded above.

## Visual provenance

`images/workspace.jpg` records the first milestone during a reference-solution run. `images/learning-home.jpg` records the connected-learning home with the user's black/light-grey palette. Both are original screenshots of the locally built application. The interface uses authored CSS, Lucide icons, native UI/code fonts, and actual numerical example bars. There are no generated photographs or invented commercial claims.

## Reproduction

```sh
pnpm install --frozen-lockfile
python -m pip install numpy==2.4.5
pnpm check
pnpm exec playwright install chromium firefox webkit
pnpm test:e2e
pnpm audit --prod
```

On Linux, install browser OS dependencies with `pnpm exec playwright install --with-deps`. GitHub uses this path. The browser suite starts the two-origin preview server automatically when needed.
