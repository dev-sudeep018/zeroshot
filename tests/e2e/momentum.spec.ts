import { test, expect } from "@playwright/test";
import { readFileSync } from "node:fs";

test("ZeroShot preserves old work, offers chosen goals, and supports quiet mode across tabs", async ({
  page,
  context,
}) => {
  await page.goto("/progress/");
  await expect(page).toHaveTitle(/ZeroShot/);
  await expect(
    page.getByRole("link", { name: "ZeroShot", exact: true }),
  ).toBeVisible();
  await page.evaluate(() =>
    localStorage.setItem("mastery:progress:m02:v1", "complete"),
  );
  await page.reload();
  const panel = page.getByRole("region", { name: "Learning momentum" });
  await expect(
    panel.getByText("10 XP · 90 to your next level", { exact: true }),
  ).toBeVisible();
  await panel.getByRole("radio", { name: "2 lessons", exact: true }).check();
  await expect(
    panel.getByText("0 / 2 lessons this week", { exact: true }),
  ).toBeVisible();
  await panel
    .getByRole("combobox", { name: "Choose a focus" })
    .selectOption("beginner-arrays");
  const home = await context.newPage();
  await home.goto("/learn/");
  await expect(
    home
      .getByRole("region", { name: "Learning momentum" })
      .getByRole("heading", { name: "Reason with arrays and measurements" }),
  ).toBeVisible();
  await panel
    .getByRole("checkbox", { name: "Show XP and milestones" })
    .uncheck();
  await expect(
    home.getByRole("region", { name: "Learning momentum" }),
  ).toHaveCount(0);
  await expect(
    panel.getByText("Quiet mode is on.", { exact: false }),
  ).toBeVisible();
  await page.reload();
  await expect(
    panel.getByRole("checkbox", { name: "Show XP and milestones" }),
  ).not.toBeChecked();
  await panel.getByRole("checkbox", { name: "Show XP and milestones" }).check();
  await expect(
    panel.getByRole("combobox", { name: "Choose a focus" }),
  ).toHaveValue("beginner-arrays");
  await home.close();
});

test("a real full-suite success awards once; visits and sample runs do not", async ({
  page,
}) => {
  await page.goto("/problems/stable-softmax/");
  await page.getByRole("tab", { name: "Solution", exact: true }).click();
  await page.getByRole("button", { name: "Use reference in editor" }).click();
  await page.getByRole("button", { name: "Replace code", exact: true }).click();
  await page.getByRole("button", { name: "Run examples", exact: true }).click();
  await expect(page.locator(".result-summary")).toContainText("passed", {
    timeout: 50_000,
  });
  expect(
    await page.evaluate(() => localStorage.getItem("zeroshot:momentum:v1")),
  ).toBeNull();
  await page
    .getByRole("button", { name: "Check solution", exact: true })
    .click();
  await expect(page.locator(".completion-reward")).toContainText("+10 XP", {
    timeout: 50_000,
  });
  const first = await page.evaluate(() =>
    localStorage.getItem("zeroshot:momentum:v1"),
  );
  await page
    .getByRole("button", { name: "Check solution", exact: true })
    .click();
  await expect(page.locator(".completion-reward")).toHaveCount(0);
  await expect(page.locator(".result-summary")).toContainText("passed");
  expect(
    await page.evaluate(() => localStorage.getItem("zeroshot:momentum:v1")),
  ).toBe(first);
  await page.goto("/progress/");
  await expect(
    page.getByText("10 XP · 90 to your next level", { exact: true }),
  ).toBeVisible();
});

test("new backups restore choices on a new device and preserve dated credit without duplication", async ({
  page,
  context,
}) => {
  await page.goto("/progress/");
  await page.evaluate(() => {
    const now = new Date();
    const day = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, "0")}-${String(now.getDate()).padStart(2, "0")}`;
    localStorage.setItem(
      "mastery:learning:v1",
      JSON.stringify({
        "e63:v1": { completed: true, attempts: 1, updatedAt: now.getTime() },
      }),
    );
    localStorage.setItem(
      "zeroshot:momentum:v1",
      JSON.stringify({
        enabled: true,
        weeklyTarget: 4,
        track: "beginner-records",
        firstCompletions: { "e63:v1": day },
      }),
    );
  });
  await page.reload();
  const downloaded = page.waitForEvent("download");
  await page.getByRole("button", { name: "Export backup" }).click();
  const file = await downloaded;
  expect(file.suggestedFilename()).toBe("zeroshot-backup.json");
  const buffer = readFileSync((await file.path())!);
  expect(JSON.parse(buffer.toString()).version).toBe(2);
  await page.evaluate(() => localStorage.clear());
  await page.reload();
  for (let i = 0; i < 2; i++) {
    await page.locator('input[type="file"]').setInputFiles({
      name: "saved.json",
      mimeType: "application/json",
      buffer,
    });
    await page.getByRole("button", { name: "Merge backup" }).click();
  }
  await expect(
    page.getByRole("radio", { name: "4 lessons", exact: true }),
  ).toBeChecked();
  await expect(
    page.getByText("1 / 4 lessons this week", { exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("10 XP · 90 to your next level", { exact: true }),
  ).toBeVisible();
  await context.clearCookies();
});

test("momentum remains readable on a narrow screen and malformed storage recovers", async ({
  page,
}) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/progress/");
  await page.evaluate(() =>
    localStorage.setItem("zeroshot:momentum:v1", '{"weeklyTarget":-1}'),
  );
  await page.reload();
  await expect(
    page.getByRole("radio", { name: "No goal", exact: true }),
  ).toBeChecked();
  await page
    .getByRole("combobox", { name: "Choose a focus" })
    .selectOption("deep-learning");
  await page.getByText("How practice credit works", { exact: true }).click();
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= innerWidth,
    ),
  ).toBe(true);
  await expect(page.getByRole("link", { name: "Browse freely" })).toBeVisible();
});
