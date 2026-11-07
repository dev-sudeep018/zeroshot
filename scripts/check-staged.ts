import { readFile, realpath } from "node:fs/promises";
import { spawnSync } from "node:child_process";
import path from "node:path";
import { loadPyodide } from "pyodide";
import { loadContent, loadPackages, root } from "./content";
import { validateCatalog } from "../packages/problem-schema/src/index";

// Validate an entire authoring batch without changing the published manifest.
const [directory, expected, ...extra] = process.argv.slice(2);
if (!directory || !/^[1-9]\d*$/.test(expected ?? "") || extra.length)
  throw new Error(
    "Usage: pnpm content:stage <draft-directory> <expected-count>",
  );
const base = await realpath(path.resolve(root, directory));
const publishedBase = await realpath(path.join(root, "content/problems"));
if (base === publishedBase || base.startsWith(publishedBase + path.sep))
  throw new Error(
    "Use content:check for published packages, not content:stage.",
  );
const [published, staged] = await Promise.all([
  loadContent(),
  loadPackages(base),
]);
if (staged.length !== Number(expected))
  throw new Error(
    `Expected ${expected} draft packages; found ${staged.length}.`,
  );
if (staged.some((entry) => entry.problem.status !== "draft"))
  throw new Error("Staged packages must retain draft status until reviewed.");
validateCatalog([...published, ...staged].map((entry) => entry.problem));

const tasks = new Map<string, string>();
for (const entry of [...published, ...staged]) {
  const key = entry.lesson.task
    .toLowerCase()
    .replace(/\d+(?:\.\d+)?/g, "#")
    .replace(/\s+/g, " ")
    .trim();
  const previous = tasks.get(key);
  if (previous && staged.includes(entry))
    throw new Error(
      `Duplicate task wording: ${previous} and ${entry.problem.id}`,
    );
  tasks.set(key, entry.problem.id);
}
const native = spawnSync(
  process.env.PYTHON ?? "python",
  ["scripts/check-staged.py"],
  {
    cwd: root,
    input: JSON.stringify(staged),
    encoding: "utf8",
    env: { ...process.env, PYTHONIOENCODING: "utf-8" },
    maxBuffer: 4 * 1024 * 1024,
  },
);
process.stdout.write(native.stdout ?? "");
process.stderr.write(native.stderr ?? "");
if (native.error) throw native.error;
if (native.status !== 0) process.exit(native.status ?? 1);

const helpers = await readFile(
  path.join(root, "content/evaluator_helpers.py"),
  "utf8",
);
const pyodide = await loadPyodide({
  indexURL: path.join(root, "apps/runner/public/runtime/"),
});
await pyodide.loadPackage("numpy");
let cases = 0;
for (const entry of staged) {
  pyodide.globals.set("__evaluator", helpers + "\n" + entry.tests);
  pyodide.globals.set("__submission", entry.solution);
  pyodide.globals.set("__starter", entry.starter);
  const raw = await pyodide.runPythonAsync(`
import json as _json
_checks, _learner, _starter = {}, {}, {}
exec(compile(__evaluator, "tests_public.py", "exec"), _checks)
exec(compile(__submission, "solution.py", "exec"), _learner)
exec(compile(__starter, "starter.py", "exec"), _starter)
_json.dumps({"reference": _checks["run_tests"](_learner, "all"),
             "starter": _checks["run_tests"](_starter, "all")})
`);
  if (typeof raw !== "string") throw new Error("Invalid WebAssembly result");
  const result = JSON.parse(raw) as {
    reference: { name: string; passed: boolean }[];
    starter: { name: string; passed: boolean }[];
  };
  const failed = result.reference.filter((test) => !test.passed);
  if (
    result.reference.length !== entry.lesson.test_count ||
    failed.length ||
    result.starter.every((test) => test.passed)
  )
    throw new Error(
      `${entry.problem.id}: WebAssembly validation failed: ${JSON.stringify(result)}`,
    );
  cases += result.reference.length;
}
console.log(
  `Staged gate passed: ${staged.length} drafts / ${cases} public cases in native and WebAssembly Python. Catalog unchanged. Independent topic oracles, editorial review and browser CI are still required for publication.`,
);
