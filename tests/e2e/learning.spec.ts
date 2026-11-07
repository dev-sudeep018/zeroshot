import { test, expect } from "@playwright/test";
import { readFileSync, readdirSync } from "node:fs";
import { parse } from "yaml";

const items = readdirSync("content/problems")
  .map((folder) => {
    const problem = parse(
      readFileSync(`content/problems/${folder}/problem.yaml`, "utf8"),
    ) as {
      id: string;
      slug: string;
      title: string;
      kind: string;
      status: string;
    };
    const lesson = JSON.parse(
      readFileSync(`content/problems/${folder}/lesson.json`, "utf8"),
    ) as { test_count: number };
    return { ...problem, ...lesson };
  })
  .filter((item) => item.status === "validated");
const lessonCount = items.filter((item) => item.kind !== "project").length;
for (const item of items) {
  test(`published reference runs in isolation: ${item.id}`, async ({
    page,
  }) => {
    await page.goto(`/problems/${item.slug}/`);
    await expect(page.getByRole("heading", { level: 1 })).toHaveText(
      item.title,
    );
    await page.getByRole("tab", { name: "Solution", exact: true }).click();
    await page.getByRole("button", { name: "Use reference in editor" }).click();
    await page
      .getByRole("button", { name: "Replace code", exact: true })
      .click();
    await page
      .getByRole("button", { name: "Check solution", exact: true })
      .click();
    await expect(
      page.getByText(`${item.test_count}/${item.test_count} passed`, {
        exact: true,
      }),
    ).toBeVisible({ timeout: 50_000 });
    expect(
      await page.evaluate(
        (id) =>
          JSON.parse(localStorage.getItem(`mastery:draft:${id}:v1`)!).code,
        item.id,
      ),
    ).toContain("def ");
  });
}
test("three learning entry points, filters, and experiments connect", async ({
  page,
}) => {
  await page.goto("/learn/");
  await page.getByRole("link", { name: "Choose a learning path" }).click();
  await page.getByRole("link", { name: "View this path" }).first().click();
  await expect(page.getByRole("heading", { level: 1 })).toHaveText(
    "Mathematics to Machine Learning",
  );
  await page.getByRole("link", { name: "Continue here", exact: true }).click();
  await expect(page.getByRole("heading", { level: 1 })).toHaveText(
    "Vector Operations and Cosine Similarity",
  );
  await page.getByRole("link", { name: "Open lab", exact: true }).click();
  await page.getByRole("button", { name: "Vector direction" }).click();
  const angle = page.getByRole("slider", { name: "Angle between vectors" });
  await angle.press("End");
  await expect(page.locator(".measurement")).toHaveText("-1.000");
  await page.getByRole("link", { name: "Lesson library", exact: true }).click();
  await page
    .getByRole("textbox", { name: "Search lessons" })
    .fill("scaled dot-product");
  await expect(page.locator(".lesson-row")).toHaveCount(1);
  await page
    .getByRole("combobox", { name: "Topic", exact: true })
    .selectOption("foundations");
  await expect(page.getByText("No matching lessons yet.")).toBeVisible();
  await page.getByRole("button", { name: "Reset filters" }).click();
  await expect(page.locator(".lesson-row")).toHaveCount(
    Math.min(lessonCount, 24),
  );
});
test("project metrics respond, notes persist, and report is downloadable", async ({
  page,
}) => {
  await page.goto("/projects/mini-retrieval/");
  await page.getByRole("slider", { name: "Results per query" }).press("Home");
  const before = await page
    .locator("tbody tr")
    .first()
    .locator("td")
    .first()
    .textContent();
  await page.getByRole("slider", { name: "Results per query" }).press("End");
  await expect(
    page.locator("tbody tr").first().locator("td").first(),
  ).toHaveText("1.000");
  expect(before).not.toBe("1.000");
  await page
    .getByRole("textbox", { name: "Your findings" })
    .fill(
      "More results improved recall; this tiny dataset cannot establish production quality.",
    );
  await page.reload();
  await expect(
    page.getByRole("textbox", { name: "Your findings" }),
  ).toHaveValue(/More results/);
  const download = page.waitForEvent("download");
  await page.getByRole("button", { name: "Export experiment report" }).click();
  const file = await download;
  const contents = JSON.parse(readFileSync((await file.path())!, "utf8"));
  expect(contents.findings).toContain("More results");
  expect(contents.experiment.rows).toHaveLength(4);
  expect(contents.provenance).toContain("synthetic");
});
test("backup import preserves existing drafts and merges completion", async ({
  page,
  context,
}) => {
  await page.goto("/progress/");
  await page.evaluate(() =>
    localStorage.setItem(
      "mastery:draft:m02:v1",
      JSON.stringify({ version: 1, code: "# keep this" }),
    ),
  );
  const openLesson = await context.newPage();
  await openLesson.goto("/problems/stable-softmax/");
  await expect(openLesson.locator(".monaco-editor .view-lines")).toContainText(
    /#\s*keep\s*this/,
  );
  const backup = {
    format: "project-mastery-backup",
    version: 1,
    progress: {
      "m02:v1": { updatedAt: 1, completed: true, attempts: 2 },
      "p01:v1": { updatedAt: 1, completed: true, attempts: 1 },
    },
    drafts: {
      "mastery:draft:m02:v1": "# incoming",
      "mastery:draft:e01:v1": "# new draft",
    },
  };
  await page.locator('input[type="file"]').setInputFiles({
    name: "backup.json",
    mimeType: "application/json",
    buffer: Buffer.from(JSON.stringify(backup)),
  });
  await page.getByRole("button", { name: "Merge backup" }).click();
  await expect(
    page.getByText(`1 of ${lessonCount} lessons checked.`, { exact: false }),
  ).toBeVisible();
  await expect(
    page.getByText("Retrieval pipeline checked.", { exact: false }),
  ).toBeVisible();
  await expect(
    openLesson.getByText("Completed on this device", { exact: true }),
  ).toBeVisible();
  await openLesson.close();
  expect(
    await page.evaluate(
      () => JSON.parse(localStorage.getItem("mastery:draft:m02:v1")!).code,
    ),
  ).toBe("# keep this");
  expect(
    await page.evaluate(
      () => JSON.parse(localStorage.getItem("mastery:draft:e01:v1")!).code,
    ),
  ).toBe("# new draft");
  await page.goto("/problems/text-chunking/");
  await expect(page.locator(".monaco-editor .view-lines")).toContainText(
    /#\s*new\s*draft/,
  );
});
test("learning pages fit a narrow viewport", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  for (const route of [
    "/learn/",
    "/paths/ai-engineering/",
    "/explore/",
    "/problems/",
    "/projects/mini-retrieval/",
    "/progress/",
  ]) {
    await page.goto(route);
    expect(
      await page.evaluate(
        () => document.documentElement.scrollWidth <= innerWidth,
      ),
      route,
    ).toBe(true);
    await expect(page.getByRole("heading", { level: 1 })).toBeVisible();
    const menu = page.getByRole("button", {
      name: "Toggle learning navigation",
    });
    if (await menu.isVisible()) await menu.click();
    const firstLink = page.getByRole("link", {
      name: "Learning home",
      exact: true,
    });
    const bounds = await firstLink.boundingBox();
    expect(
      bounds?.x,
      `${route}: first navigation link is reachable`,
    ).toBeGreaterThanOrEqual(0);
    await firstLink.click();
    await expect(page).toHaveURL("http://localhost:3000/learn/");
  }
});
