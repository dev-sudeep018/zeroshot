# Free resources and a faster curriculum workflow

The 23 October [exercise-platform follow-up](platform-pilot.md) adds TensorTonic,
Deep-ML, Pyre-Code and HappyTorch to the registry, bringing it to 25 resources.
Six Pyre-Code activities are adapted with MIT notices and original tests. That
follow-up records which platforms permit our intended reuse and which stay external.

Checked 22 October 2026. The first survey covers 21 sources: 18 GitHub
repositories plus Google ML Crash Course, MIT OpenCourseWare, and a verified UCI
dataset. Repository metadata, license files, and selected official course pages
were inspected. This is a useful starting set, not an exhaustive survey of the
internet or a claim that all upstream exercises have been reviewed or executed.

The machine-readable [source registry](../content/sources.json) records URLs,
Git revisions where available, license evidence, topics, runtime fit, and a reuse
decision for each source. No third-party lessons or datasets were imported
during that initial survey; the registry does not increase the published problem count.
The [23 October batch](curriculum-batch-03.md) uses these findings for 30 new
activities, including one credited D2L code adaptation with its original notice.

## Best starting points

| Resource                                                                                        | Useful contribution                                         | Verified license / handling                                                        | Fit for the current product                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| [NumPy tutorials](https://github.com/numpy/numpy-tutorials)                                     | Array operations, linear algebra, numerical investigations  | BSD three-clause text in LICENSE.txt; preserve notices                             | Adapt small kernels; remove plotting/download dependencies                                                      |
| [100 NumPy exercises](https://github.com/rougier/numpy-100)                                     | Broad array/indexing practice                               | Repository MIT; README identifies mixed origins, so inspect each item's provenance | Expand selected exercises into explanations, debugging, and experiments; do not bulk-count 100 imported prompts |
| [Dive into Deep Learning](https://github.com/d2l-ai/d2l-en)                                     | A coherent mathematical and deep-learning sequence          | CC BY-SA 4.0 prose; modified MIT/MIT-0 sample code in separate license             | Strong source for NumPy adaptations and connected paths                                                         |
| [Microsoft ML for Beginners](https://github.com/microsoft/ML-For-Beginners)                     | Applied regression, classification, clustering and projects | MIT repository                                                                     | Extract small offline activities; full scikit-learn/R projects need more runtime support                        |
| [Microsoft Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners) | Data cleaning, statistics, and investigation                | MIT repository                                                                     | Good source for supplied-array experiments                                                                      |
| [Hugging Face LLM Course](https://github.com/huggingface/llm-course)                            | Tokenization, datasets, language-model concepts             | Apache-2.0 repository                                                              | Tokenization mechanics fit; model training/downloads need external notebooks                                    |
| [scikit-learn examples](https://scikit-learn.org/stable/auto_examples/index.html)               | Preprocessing, model comparison, evaluation                 | BSD-3-Clause repository; inspect per-file/data exceptions                          | Port bounded numerical tasks; sklearn/SciPy are not currently allowed runner packages                           |
| [micrograd](https://github.com/karpathy/micrograd)                                              | A small inspectable automatic-differentiation system        | MIT                                                                                | Strong basis for a multi-step autograd project with independent tests                                           |
| [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)           | Short explanations, predictions and conceptual checks       | Inspected linear-regression page: CC BY 4.0 prose, Apache-2.0 code                 | Adapt eligible text/code with attribution; media and third-party content require separate checks                |
| [UCI Iris](https://archive.ics.uci.edu/dataset/53/iris)                                         | A small real classification dataset                         | CC BY 4.0 for this dataset, DOI 10.24432/C56C76                                    | Bundle a versioned, attributed dataset after import checks; verify other UCI datasets individually              |

License evidence and immutable repository links are in the registry. In
particular, [D2L's sample-code license](https://github.com/d2l-ai/d2l-en/blob/master/LICENSE-SAMPLECODE)
differs from its prose license; a repository's single GitHub license badge can
miss that distinction.

## Other sources inspected

| Resource                                                                                          | Best use                                       | Handling                                                                                              |
| ------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [Microsoft AI for Beginners](https://github.com/microsoft/AI-For-Beginners)                       | Vision/NLP and neural-network projects         | MIT; framework notebooks need adaptation or native execution                                          |
| [Microsoft Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) | Retrieval and AI application design            | MIT; free lessons may still use paid APIs or credentials                                              |
| [Hugging Face Agents Course](https://github.com/huggingface/agents-course)                        | Tool traces, agent evaluation and projects     | Apache-2.0; start with offline fixtures before hosted tools                                           |
| [Hugging Face Deep RL Course](https://github.com/huggingface/deep-rl-class)                       | Reinforcement-learning progression             | Apache-2.0; tabular calculations fit before simulator-based training                                  |
| [PyTorch tutorials](https://github.com/pytorch/tutorials)                                         | Autograd, training, profiling and serving      | BSD-3-Clause; torch is outside today's browser runtime                                                |
| [Hands-On ML notebooks](https://github.com/ageron/handson-ml3)                                    | Applied projects and comparisons               | Repository Apache-2.0; the separate book and datasets are not automatically covered                   |
| [Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)                      | Backpropagation and language-model progression | MIT repository; do not extend that license to linked videos                                           |
| [Spinning Up](https://github.com/openai/spinningup)                                               | Returns, value functions and policy methods    | MIT; inspect legacy dependencies before executing training code                                       |
| [fast.ai book](https://github.com/fastai/fastbook)                                                | Linked reading and project inspiration         | Code GPL v3; README restricts prose redistribution. Link rather than import into our current packages |
| [fast.ai course notebooks](https://github.com/fastai/course22)                                    | Linked practical course                        | No repository license returned by the inspected license endpoint; copying permission not established  |
| [MIT OpenCourseWare](https://ocw.mit.edu/)                                                        | Linked mathematical background                 | CC BY-NC-SA 4.0 with exceptions; keep separate from this project's CC BY-SA content                   |

The [fastbook README](https://github.com/fastai/fastbook#readme),
[MIT OCW terms](https://ocw.mit.edu/pages/privacy-and-terms-of-use/), and
[Google site policies](https://developers.google.com/terms/site-policies)
explain the important differences. Free access, open reuse, and free execution
are separate questions. Images, datasets, model weights, and external services
do not inherit a course repository's license automatically.

## How this changes production

Work in topic batches of roughly 25–50 distinct objectives. This is a batching
policy, not a promised delivery rate. Start with NumPy/data preparation, then
probability/evaluation, then autograd and tokenization. Reuse the established
reading/editor/feedback interface; content-only batches do not need a redesign.
The [production workflow](content-production.md) now provides a reusable batch
packager, one tested build shared across browsers, and parallel execution of
the full browser suite.

For each candidate, record its source revision and exact section, the learning
objective, misconception to expose, required runtime, and attribution obligations.
Turn it into an activity: predict a result, repair a defect, compare alternatives,
or build a component used by a project. Do not count translations, renamed
variables, or changed numbers as distinct problems.

Use the existing six-file package contract for all activities. Preserve upstream
license notices in adapted files, record modifications, and add an attribution
entry. The current schema only labels our original prose/code licenses; before
importing differently licensed material, extend provenance to record the actual
per-file upstream terms rather than silently relabeling it.

During authoring, run the fast batch check:

```sh
pnpm content:check m05 m06 m07 d05 d06 d07 e05 e06 e07
```

It validates the complete metadata/prerequisite graph, then executes selected
references, incomplete starters, trivial wrong answers, and sample/test counts.
It also flags identical task wording after numerical substitutions. That flag
is only a review aid, not semantic deduplication. Omit IDs to check all packages.
Unknown IDs fail rather than silently testing nothing.

This command does not build the frontend or reinstall runtime assets. Use it
after a content edit; run the independent numerical/misconception tests as the
batch develops. `pnpm check` remains the full release gate, followed by browser
CI covering every published reference in Chromium, Firefox, and WebKit. Native
Python tests now run once in `pnpm check`, instead of twice. Manual UI review is
for changed components and new interaction formats; editorial review still
assesses every new objective, explanation, and test contract.

Large GPU/API notebooks should become explicitly linked external projects until
we implement an appropriate execution path. This keeps the free core usable and
avoids presenting incompatible notebooks as browser-runnable lessons.
