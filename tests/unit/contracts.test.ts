import { describe, expect, it } from "vitest";
import {
  ProblemSchema,
  validateCatalog,
} from "../../packages/problem-schema/src/index";
import {
  assertSeparateOrigin,
  RunRequestSchema,
  RunnerMessageSchema,
} from "../../packages/runner-protocol/src/index";
import { readDraft } from "../../apps/web/src/lib/draft";
import { loadContent } from "../../scripts/content";

describe("versioned content", () => {
  it("loads complete content packages", async () => {
    const entries = await loadContent();
    expect(entries.filter((e) => e.problem.kind === "lesson")).toHaveLength(
      450,
    );
    expect(entries.filter((e) => e.problem.kind === "project")).toHaveLength(1);
    for (const entry of entries) {
      expect(entry.tests).toContain("run_tests");
      expect(entry.lesson.signature).toContain(
        entry.problem.evaluation.entrypoint,
      );
    }
  });
  it("rejects missing prerequisites and cycles", async () => {
    const [{ problem }] = await loadContent();
    expect(() =>
      validateCatalog([{ ...problem, prerequisites: ["m01"] }]),
    ).toThrow("Missing");
    expect(() =>
      validateCatalog([{ ...problem, prerequisites: [problem.id] }]),
    ).toThrow("cycle");
  });
  it("rejects duplicate IDs, unsupported runtime and extra fields", async () => {
    const [{ problem }] = await loadContent();
    expect(() => validateCatalog([problem, problem])).toThrow("Duplicate");
    expect(
      ProblemSchema.safeParse({
        ...problem,
        runtime: { engine: "server", packages: ["numpy"] },
      }).success,
    ).toBe(false);
    expect(
      ProblemSchema.safeParse({ ...problem, undocumented: true }).success,
    ).toBe(false);
  });
});
describe("untrusted messages", () => {
  const request = {
    kind: "run",
    protocol: 1,
    requestId: "8bb803a0-4ae7-4d22-8231-4223a017bcf5",
    problemId: "m02",
    problemVersion: 1,
    sourceCode: "print(1+2)",
    mode: "all",
  };
  it("accepts valid requests and rejects oversized source, unknown fields and versions", () => {
    expect(RunRequestSchema.safeParse(request).success).toBe(true);
    for (const patch of [
      { sourceCode: "x".repeat(32001) },
      { timeBudgetMs: 999999 },
      { protocol: 2 },
      { problemId: "../secrets" },
    ])
      expect(RunRequestSchema.safeParse({ ...request, ...patch }).success).toBe(
        false,
      );
  });
  it("rejects malformed and unbounded results", () => {
    expect(
      RunnerMessageSchema.safeParse({ kind: "result", status: "passed" })
        .success,
    ).toBe(false);
    expect(
      RunnerMessageSchema.safeParse({
        kind: "ready",
        protocol: 1,
        html: "<img>",
      }).success,
    ).toBe(false);
  });
  it("fails closed on same-origin configuration", () => {
    expect(() =>
      assertSeparateOrigin("http://localhost:3000", "http://localhost:3000"),
    ).toThrow();
    expect(() =>
      assertSeparateOrigin("http://localhost:3000", "javascript:alert(1)"),
    ).toThrow();
    expect(
      assertSeparateOrigin("http://localhost:3000", "http://127.0.0.1:4174"),
    ).toBe("http://127.0.0.1:4174");
  });
});
describe("local drafts", () => {
  it("restores an intentionally empty draft", () =>
    expect(readDraft('{"version":1,"code":""}', "starter")).toBe(""));
  it("recovers from malformed, obsolete and oversized drafts", () => {
    for (const value of [
      null,
      "bad json",
      '{"version":2,"code":"old"}',
      JSON.stringify({ version: 1, code: "x".repeat(32001) }),
    ])
      expect(readDraft(value, "starter")).toBe("starter");
  });
});
