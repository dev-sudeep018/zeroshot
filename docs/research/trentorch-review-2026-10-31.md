# What ZeroShot can learn from TrenTorch

Reviewed 31 October 2026. This review combines public website pages, the earlier browser walkthrough in this chat, and selected public repository files. The source snapshot used for architecture observations is commit [`dca314c33fbd4fe90e5d9cc442a537b7e9bb2e7c`](https://github.com/TrenTorch/TrenTorch/tree/dca314c33fbd4fe90e5d9cc442a537b7e9bb2e7c). It is a reference study, not a complete audit of their curriculum or a benchmark of learning outcomes. ZeroShot was previously named Project Mastery.

## Most useful lesson

TrenTorch makes small implementations feel like parts of a larger education. Its strongest transferable pattern is the connection between a concept, a realistic function contract, executable evidence, and the next related operation. ZeroShot should develop that connection alongside catalog growth. A large question count by itself does not explain where a learner should begin or what they will be able to build.

The home page presents theory, implementation, and submission as one sequence and advertises offline PyTorch comparisons, edge cases, and mutation tests. Those are the site's claims; this review did not independently execute every exercise or establish the coverage of those methods. [TrenTorch home](https://trentorch.com/)

## What was observed, and what remains unverified

| Surface                                          | Observation                                                                                                    | Interpretation                                                                                                             |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [Home](https://trentorch.com/)                   | Advertises 1,647+ problems and 12 topics. The displayed beginner/intermediate/advanced breakdown totals 1,397. | Counts may describe different collections or deployment states. Do not present one as a verified unique runnable total.    |
| [Modules](https://trentorch.com/questions)       | Displays 1,397 questions across 12 modules, with search and filters.                                           | A curriculum-first entry is useful when someone needs direction.                                                           |
| [Problem set](https://trentorch.com/problemset)  | Displays 349 problems across five study modules.                                                               | A separate flat catalog can serve targeted practice, but ZeroShot should make the relationship between its views explicit. |
| [Research papers](https://trentorch.com/papers)  | Advertises 120 papers, ten tracks, and 360 implementations.                                                    | Paper-to-implementation journeys are a useful later extension. These are advertised counts, not audited completions.       |
| [Problem of the Day](https://trentorch.com/potd) | Publicly promotes a recurring challenge, account progress, and rating.                                         | A prompt to return is a product pattern, not evidence that competitive rating improves understanding.                      |

In the browser walkthrough, the practice entry opened a sign-in dialog. No account was created and no authenticated submission was tested. Publicly accessible IDE descriptions and repository files supplied the deeper content review. The visible black/off-white interface, restrained borders, clear reading hierarchy, and compact navigation are compatible with ZeroShot's chosen palette; its red accent is not necessary to adopt.

## Teaching patterns worth adapting

**Beginner can still mean consequential.** The public [stable L2 norm exercise](https://trentorch.com/ide/problem-1-compute-a-stable-l2-norm) is labeled beginner yet asks learners to handle very large and small magnitudes safely. That is a useful example of a small contract with an authentic numerical pitfall. For ZeroShot, beginner work should limit the number of new ideas while retaining meaningful data, edge cases, and an explanation of why the operation matters.

**Small operations should converge into a system.** The inspected linear-regression track connects prediction, loss, gradient, update, and training. Its [training-loop lesson](https://github.com/TrenTorch/TrenTorch/blob/dca314c33fbd4fe90e5d9cc442a537b7e9bb2e7c/TrenTorch_Web/data/app_data/01-classical-ml/01-linear-regression/05-training-loop/README.md) explicitly reuses earlier helpers and preserves their shape contracts. ZeroShot can apply the same instructional principle with original exercises: introduce one operation, make its failure modes visible, then combine several operations in a small project. This should inform quests and milestones, so the reward describes something the learner assembled.

**Explain the dangerous detail.** The inspected [hypothesis-function lesson](https://github.com/TrenTorch/TrenTorch/blob/dca314c33fbd4fe90e5d9cc442a537b7e9bb2e7c/TrenTorch_Web/data/app_data/01-classical-ml/01-linear-regression/01-hypothesis-function/README.md) develops intuition before formal shape requirements. It addresses practical conventions and broadcasting mistakes. ZeroShot's lesson template should similarly include a tiny worked case, the general operation, one misleading result that naive code might produce, and the test that distinguishes them. This is a writing guideline, not permission to reuse their prose.

## Authoring and validation patterns

The [authoring guide](https://github.com/TrenTorch/TrenTorch/blob/TrenTorch-Dev/TrenTorch_Web/data/app_data/README.md) keeps metadata and teaching text together in Markdown, while starters, references, and tests remain real Python files. Generated runtime JSON is a build artifact. Sections, tracks, and lessons have an explicit order separate from their stable identities. It also explains why shared dependency imports need unique names and full-suite validation.

ZeroShot already has per-item metadata, prose, starters, reference implementations, and cases. The practical improvement is a track-level plan around those packages: intended outcome, prerequisites, ordered operations, and a small integration checkpoint. Keep reviewable source files as the authority and generate catalog views and counts from validated content. Do not migrate file formats simply because another project uses Markdown.

The inspected [Pyodide test suite](https://github.com/TrenTorch/TrenTorch/blob/dca314c33fbd4fe90e5d9cc442a537b7e9bb2e7c/TrenTorch_Web/pyodide-check/questions.spec.ts) runs reference answers through the same sanitizer, runner-script builder, and harness used by its web runtime. It checks runtime-version consistency and maintains an explicit failure baseline. That is useful protection against native-Python/browser differences. The observed empty baseline is a source-file observation, not proof of a successful CI run.

The [harness](https://github.com/TrenTorch/TrenTorch/blob/dca314c33fbd4fe90e5d9cc442a537b7e9bb2e7c/TrenTorch_Web/processes/ide-content/build-test-harness.ts) distinguishes dependencies required before a learner's definitions from tests run afterward and isolates dependency namespaces. This matters if ZeroShot later lets one exercise use helpers from another. Implement such composition deliberately, with failure messages that identify authoring problems instead of blaming learner code.

Their [CI workflow](https://github.com/TrenTorch/TrenTorch/blob/dca314c33fbd4fe90e5d9cc442a537b7e9bb2e7c/.github/workflows/ci.yml) separates curriculum and runtime checks and uses changed-path filtering. Its named smoke tests inspect static HTML; that is not equivalent to running a real interactive browser. ZeroShot should retain its own browser execution and isolation checks. Faster targeted feedback can complement a complete release gate, not replace it.

## Gamification fit for ZeroShot

Adopt the invitation to take a concrete next step, together with visible completion and understandable milestones. Adapt the recurring-challenge idea into an optional weekly goal chosen by the learner. Favor a track quest that fits prerequisites over a mandatory daily problem of arbitrary difficulty. Offer an ordinary library alongside these suggestions.

The first layer should use checked-practice XP, a small practice-level progression, beginner-track achievements, and a project checkpoint. Keep the rule transparent and the experience optional. Repeated runs, opening pages, or repeatedly importing progress should not produce additional rewards. Never describe a passing reference-based test result as proof of long-term mastery. The accompanying [gamification evidence and implementation plan](./gamification-evidence.md) explains the research, state rules, evaluation, and later spaced-review design.

## Reuse boundary and priorities

The inspected repository uses [PolyForm Noncommercial 1.0.0](https://github.com/TrenTorch/TrenTorch/blob/TrenTorch-Dev/LICENSE), including a noncommercial-purpose restriction and required notice. Public availability is not an Apache/MIT grant. This review uses product and architecture observations; it does not import TrenTorch code, tests, or lesson text into ZeroShot.

1. **Now:** implement personal progress, chosen quests, transparent rewards, and portable state without disrupting the editor or existing saved work.
2. **Next:** improve track coherence and explanations, pairing small operations with integration checkpoints. Audit difficulty by prerequisites and conceptual load rather than copying labels.
3. **Then:** add genuine retrieval review and more project journeys. Introduce paper-to-code tracks only when the prerequisite path and implementation checks are ready.

Use one generated, clearly defined count for ZeroShot's runnable published lessons. Keep draft counts, projects, experiments, and planned curriculum separate so catalog growth remains understandable and verifiable.
