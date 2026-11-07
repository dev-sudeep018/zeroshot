import { readFile, readdir } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { parse } from "yaml";
import {
  ProblemSchema,
  LessonSchema,
  validateCatalog,
} from "../packages/problem-schema/src/index";

export const root = fileURLToPath(new URL("../", import.meta.url));
export async function loadContent() {
  const entries = await loadPackages(path.join(root, "content/problems"));
  validateCatalog(entries.map((e) => e.problem));
  return entries;
}

/** Read packages without assuming their prerequisites are in this directory. */
export async function loadPackages(base: string) {
  const dirs = await readdir(base, { withFileTypes: true });
  const entries = await Promise.all(
    dirs
      .filter((d) => d.isDirectory())
      .map(async (d) => {
        const dir = path.join(base, d.name);
        const problem = ProblemSchema.parse(
          parse(await readFile(path.join(dir, "problem.yaml"), "utf8")),
        );
        const files = await Promise.all(
          [
            "starter.py",
            "solution.py",
            "tests_public.py",
            "explanation.md",
          ].map((f) => readFile(path.join(dir, f), "utf8")),
        );
        if (files.some((f) => !f.trim()))
          throw new Error(`Empty required file in ${d.name}`);
        return {
          folder: d.name,
          problem,
          lesson: LessonSchema.parse(
            JSON.parse(await readFile(path.join(dir, "lesson.json"), "utf8")),
          ),
          starter: files[0],
          solution: files[1],
          tests: files[2],
          explanation: files[3],
        };
      }),
  );
  return entries.sort((a, b) => a.problem.id.localeCompare(b.problem.id));
}
