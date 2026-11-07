# Faster curriculum production

Work in batches of 25–50 distinct learning objectives, using compatible licensed
sources and the existing interface. This is the batch size to aim for, not a
promised delivery rate. Authored examples, useful feedback and independently
checked mathematics remain the work that makes an activity worth publishing.

## One batch file, one packager

`scripts/author-batch.py` replaces the disposable per-batch generators previously
kept under `work/`. Its JSON input holds the original teaching prose, NumPy
implementation, public cases and exact upstream source records. The tracked
`scripts/authoring/example.json` reuses the existing M18 lesson as an executable
format example; it is not a new activity.

For an already inspected, pinned source-text snapshot:

```sh
pnpm content:author scripts/authoring/example.json --snapshot work/upstream/pyre-code --output work/m18-review --dry-run
pnpm content:author scripts/authoring/example.json --snapshot work/upstream/pyre-code --output work/m18-review
```

The snapshot must contain the exact `LICENSE` and task files named in the JSON.
Both normal repository paths and the existing flat cache names are supported.
The packager checks source and license hashes, syntax, required teaching fields,
unique IDs/slugs, and the correspondence between worked examples and sample cases.
It reads upstream files as bytes and never imports or executes them.

It creates seven files per lesson and a provenance manifest. Full MIT notices
stay in each reference and notice file. Every output is marked `draft`; the tool
refuses an existing output directory and direct output into the published catalog.
All entries are validated before writing begins. Filesystem failures can still
leave an incomplete review directory; inspect it instead of overwriting it.

The current adapter handles reviewed MIT source code with original prose and
NumPy implementations. It is not a blanket importer for arbitrary repositories,
licenses or task descriptions. Its validation is a preflight check; the project’s
content schemas and prerequisite checks remain authoritative.

## Short development loop, one release gate

1. Select distinct objectives for the whole topic batch and inspect their source
   operations. Existing aliases, fork duplicates and number swaps do not count.
2. Write one JSON batch using the example format. Include the finite-value bounds
   used by the shared helpers in each lesson’s requirements.
3. Generate into a new review directory. Review the output, move new packages
   into `content/problems`, and record the manifest under `content/` with final
   notice paths and inspection date. Keep drafts unpublished during development.
4. Run `pnpm content:check` with the batch IDs. Add independent property or oracle
   checks for the new concepts. Revise the batch data or generated files as needed;
   the packager deliberately does not overwrite edited packages.
5. After editorial and mathematical review, mark accepted packages validated,
   connect them to paths, format changed files and run `pnpm check` once.
6. Execute the new references in the browser and submit one batch PR. GitHub runs
   the full browser suite. Recheck layouts when components or interaction formats
   change; a content-only batch does not need a fresh visual redesign.

## Reuse the tested build

CI runs on pull requests and pushes to `main`. A feature-branch push with an open
PR starts one workflow, instead of separate push and PR workflows. Create the PR
to start feature-branch CI; unopened feature branches no longer run automatically.

The quality job performs one complete check/build and uploads the static site and
isolated runner. Chromium, Firefox and WebKit download that same build. Their
required check names stay unchanged. This removes seven of the eight builds that
previously ran for a feature update with an open PR, while retaining every test.
See [GitHub’s artifact workflow documentation](https://docs.github.com/en/actions/tutorials/store-and-share-data).

Browser tests use two workers with independent browser contexts and Python
workers. Concurrency is bounded because each Python runtime consumes memory.
All tests still run; `--workers=1` remains available for diagnosis. See
[Playwright’s parallel-test documentation](https://playwright.dev/docs/test-parallel).

`pnpm check` also reuses its initial setup when invoking the final build.
Standalone `pnpm build` still prepares its own required assets.
