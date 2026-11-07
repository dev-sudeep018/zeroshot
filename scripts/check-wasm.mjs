// Run the published references against the same pinned WebAssembly Python and
// generated evaluators as the app, before slower browser/isolation checks.
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { loadPyodide } from "pyodide";

const root = fileURLToPath(new URL("../", import.meta.url));
const readJson = async (name) =>
  JSON.parse(await readFile(path.join(root, name), "utf8"));
const manifest = await readJson("apps/runner/src/generated/manifest.json");
const catalog = await readJson("apps/web/src/generated/catalog.json");
const selected = new Set(process.argv.slice(2));
for (const id of selected) {
  if (!manifest.some((item) => item.id === id))
    throw new Error(`Unknown published item: ${id}`);
}
const pyodide = await loadPyodide({
  indexURL: path.join(root, "apps/runner/public/runtime/"),
});
await pyodide.loadPackage("numpy");
let packages = 0;
let cases = 0;
for (const item of manifest) {
  if (selected.size && !selected.has(item.id)) continue;
  const meta = catalog.find((entry) => entry.id === item.id);
  const data = await readJson(`apps/web/src/generated/items/${meta.slug}.json`);
  const evaluator = await readFile(
    path.join(root, "apps/runner/public", item.evaluator),
    "utf8",
  );
  pyodide.globals.set("__evaluator", evaluator);
  pyodide.globals.set("__submission", data.solution);
  const result = JSON.parse(
    await pyodide.runPythonAsync(`
import json as _json
_checks = {"__name__": "__checks__"}
_learner = {"__name__": "__main__"}
exec(compile(__evaluator, "tests_public.py", "exec"), _checks)
exec(compile(__submission, "solution.py", "exec"), _learner)
_json.dumps(_checks["run_tests"](_learner, "all"))
`),
  );
  const failed = result.filter((test) => !test.passed);
  if (result.length !== data.lesson.test_count || failed.length)
    throw new Error(
      `${item.id}: ${JSON.stringify({ count: result.length, failed })}`,
    );
  packages++;
  cases += result.length;
}
console.log(
  `WebAssembly references passed: ${packages} packages / ${cases} public cases.`,
);
