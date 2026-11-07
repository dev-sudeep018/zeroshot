import { test, expect } from "@playwright/test";
import { readFileSync, readdirSync } from "node:fs";
import { parse } from "yaml";

// CI browser jobs consume the quality job's static export. Source-generated
// application modules are intentionally not required by these tests.
const catalog = readdirSync("content/problems")
  .map(
    (folder) =>
      parse(
        readFileSync(`content/problems/${folder}/problem.yaml`, "utf8"),
      ) as {
        id: string;
        kind?: string;
        status: string;
        difficulty: string;
        domain: string;
        title: string;
        slug: string;
      },
  )
  .filter((item) => item.status === "validated" && item.kind !== "project");
const startingPoints = [
  "e63",
  "e65",
  "e66",
  "e69",
  "e72",
  "e73",
  "m60",
  "m61",
  "m62",
  "m63",
  "m65",
  "m67",
  "d80",
  "d84",
  "d85",
  "d90",
  "d95",
  "d100",
];

const beginnerCount = catalog.filter(
  (item) => item.difficulty === "beginner",
).length;

test("beginner route is reachable and reuses published lessons and progress", async ({
  page,
}) => {
  await page.addInitScript((key) => {
    localStorage.setItem(
      key,
      JSON.stringify({
        "e63:v1": { updatedAt: 1, completed: true, attempts: 1 },
      }),
    );
  }, "mastery:learning:v1");
  await page.goto("/paths/");
  await page.getByRole("link", { name: "Explore the beginner route" }).click();
  await expect(page).toHaveURL(/\/paths\/start-here\//);
  await expect(page.getByRole("heading", { level: 1 })).toHaveText(
    "Start small. Build something useful.",
  );
  await expect(page.locator(".path-list > li")).toHaveCount(
    startingPoints.length,
  );
  await expect(page.locator(".learning-path").first()).toContainText(
    "1/6 checked",
  );
  await expect(
    page.getByRole("link", { name: "Revisit the idea", exact: true }),
  ).toHaveCount(1);
  for (const id of startingPoints) {
    const item = catalog.find((entry) => entry.id === id)!;
    await expect(
      page.getByRole("link", { name: item.title, exact: true }),
    ).toHaveAttribute("href", `/problems/${item.slug}/`);
  }
  await page
    .getByRole("link", { name: "Explore all beginner lessons" })
    .click();
  await expect(page).toHaveURL(/\/beginner\//);
  await expect(page.getByRole("combobox", { name: "Depth" })).toHaveValue(
    "beginner",
  );
  await expect(page.getByRole("status")).toHaveText(
    `${beginnerCount} of ${catalog.length} published lessons`,
  );
});

test("beginner filtering works across topics and resets pagination", async ({
  page,
}) => {
  await page.goto("/beginner/");
  await page.getByRole("button", { name: "Next", exact: true }).click();
  for (const domain of ["engineering", "foundations", "deep-learning"]) {
    await page
      .getByRole("combobox", { name: "Topic", exact: true })
      .selectOption(domain);
    const count = catalog.filter(
      (item) => item.domain === domain && item.difficulty === "beginner",
    ).length;
    await expect(page.getByRole("status")).toHaveText(
      `${count} of ${catalog.length} published lessons`,
    );
    await expect(
      page.locator(".lesson-state").filter({ hasText: "beginner" }),
    ).toHaveCount(Math.min(count, 24));
    if (count > 24)
      await expect(page.locator(".pagination")).toContainText("Page 1");
  }
  await page.getByRole("combobox", { name: "Depth" }).selectOption("all");
  await expect(page.getByRole("status")).toHaveText(
    `${catalog.filter((item) => item.domain === "deep-learning").length} of ${catalog.length} published lessons`,
  );
});

test("beginner pages remain usable on a narrow screen", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  for (const route of ["/paths/", "/paths/start-here/", "/beginner/"]) {
    await page.goto(route);
    await expect(page.getByRole("heading", { level: 1 })).toBeVisible();
    expect(
      await page.evaluate(
        () => document.documentElement.scrollWidth <= innerWidth,
      ),
      route,
    ).toBe(true);
  }
  await page
    .getByRole("textbox", { name: "Search lessons" })
    .fill("not-a-published-lesson-450");
  await expect(page.getByText("No matching lessons yet.")).toBeVisible();
  await page.getByRole("button", { name: "Reset filters" }).click();
  await expect(page.getByRole("status")).toHaveText(
    `${catalog.length} of ${catalog.length} published lessons`,
  );
});
