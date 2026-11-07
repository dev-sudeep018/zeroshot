# Architecture

## Boundaries

The Next.js application exports static files. A separate static runner origin serves an iframe, a bundled bridge, disposable module workers, Pyodide 314.0.7, NumPy, and versioned public evaluators. No application authentication exists in this milestone.

Locally the application uses `http://localhost:3000` and the runner uses `http://127.0.0.1:4174`. Production must use HTTPS and a separate registrable domain with no application cookies or credentials. Deployment is deferred until its exact hosting headers and origins are tested.

The iframe is sandboxed with allow-scripts and allow-same-origin. This combination is only acceptable here because it is cross-origin; a same-origin configuration is rejected by both sides. A worker is used for responsiveness and termination, not as the sole security boundary.

The host validates the iframe source window, exact origin, protocol version, request ID, and bounded result schema. The runner validates the source window and an exact, build-time parent origin. It rejects unknown fields, unsupported problem versions, and source over 32,000 characters. No user-selectable time budget exists.

## Network policy

The HTTP server supplies CSP on the frame AND worker responses: default-src none, script-src self plus wasm-unsafe-eval, worker-src self, connect-src self, no frames, objects, images, fonts, or forms, and exact frame-ancestors. `unsafe-eval`, blob workers, third-party script sources, and arbitrary outbound connections are not allowed. No CORS grants are issued. Runtime downloads happen during setup, not by learner code against external CDNs. NumPy wheel bytes are verified against the runtime lockfile SHA-256.

Learner code can request public files on the runner origin. That is an explicit allowlist boundary, not a promise of zero network access. The runner has no secrets, dynamic APIs, writes, redirects, authenticated resources, or external proxies. GET and HEAD are the only allowed methods. Do not add capabilities here casually.

## Lifecycle

Each run creates a new worker and Python environment. Boot has a 45-second deadline. Only after the runtime loads does the bridge start a separate three-second execution timer and send the submission. The bridge terminates the worker on completion, error, timeout, or cancellation. A host watchdog recreates the iframe if the bridge stops responding. Python output is capped at 4,096 characters, errors at 2,048, and tests at 40. All learner text is rendered as React text nodes.

Browser memory usage has no hard per-worker quota. A hostile learner can exhaust their own tab or device. Terminating the worker is recovery, not an OS-grade resource sandbox. The tests cover common escape attempts and failure behavior; they do not constitute an independent security audit.

## Content and assessment

YAML metadata is validated by Zod. Original Python reference solutions and public evaluators run in local/CI Python and browser Python. A problem version is immutable once publicly released; change its version when the grading contract changes. `validated` records automated validation, not external editorial review.

Structured lessons are separately validated. Setup generates a metadata catalog,
per-route content files, and a runner manifest. Both bridge and worker resolve
the exact ID/version against that manifest; requests never supply evaluator
paths. Only validated content is published. Shared evaluator helpers are
prepended identically in native and browser Python.

Client-side grading is formative. Python can modify its own runtime and forge worker results. The platform makes no tamper-resistant completion claim. A future trusted grader would require a separate server isolation design, authorization, quotas, and independently stored results.

## Persistence

Versioned drafts and completion flags stay in localStorage on the application origin. Storage errors are surfaced. No source-code uploads, tracking, accounts, or paid APIs are present. A completion flag records that the learner passed the full suite at least once; later edits do not erase that history.

The learning record adds visit timestamps and full-check attempt counts.
Legacy M02 completion remains readable. Progress views listen for cross-tab
storage changes. Export/import uses a strict versioned JSON schema; import
preserves completion, takes the latest timestamp and highest attempt count,
and fills only missing drafts for known content versions. Existing drafts
are preserved. Project notes and experiment reports are exported separately.

The retrieval workbench uses original documents and manually assigned teaching
vectors. Chunk controls preview preprocessing; ranking uses whole-document
vectors and explicitly says so. Its JavaScript baseline is separate from the
learner's Python implementation checkpoint. Neither is presented as a trained
embedding model or a production benchmark.

## References

- [Next.js static exports](https://nextjs.org/docs/app/guides/static-exports)
- [Pyodide module workers](https://pyodide.org/en/stable/usage/webworker.html)
- [MDN iframe sandbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#sandbox)
- [Monaco Editor](https://github.com/microsoft/monaco-editor)

These informed the implementation; current limitations and actual test evidence are recorded in verification.md.

## Local practice rewards and rename compatibility

ZeroShot retains `mastery:learning:v1`, per-item completion keys, and draft keys so the rename does not discard local work. Practice XP and achievements are derived from completed current catalog versions; visits and repeated runs cannot increase the score. The `zeroshot:momentum:v1` record stores optional preferences and known first-completion calendar days. Per-item `zeroshot:first-completion:<id>:v<version>` records preserve dates if another tab writes an older aggregate snapshot. Completion keys similarly recover checked status. Attempts and last-visit metadata remain best-effort local snapshots.

Only a newly successful full-suite check records a first-completion day. Historical completion with an unknown date earns current-catalog XP but receives no guessed weekly credit. Monday-to-Sunday goals use local calendar dates, including across DST boundaries. The v2 `zeroshot-backup` format carries preferences and dated progress; the strict legacy v1 `project-mastery-backup` remains accepted. Imports merge matching current versions, preserve existing drafts and preferences, and restore preferences on a fresh device. Dates are unioned conservatively using the earliest valid known day. Exported backups include the recovered per-item dates. This is personal practice feedback, not a competitive credential or synchronized account. Future lesson-version publication requires an explicit historical-credit migration policy.
