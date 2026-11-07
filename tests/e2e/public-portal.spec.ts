import { test, expect } from "@playwright/test";
import { readdirSync, readFileSync } from "node:fs";
import { parse } from "yaml";
const lessonCount = readdirSync("content/problems")
  .map((folder) =>
    parse(readFileSync(`content/problems/${folder}/problem.yaml`, "utf8")),
  )
  .filter(
    (item) => item.kind !== "project" && item.status === "validated",
  ).length;

test("public introduction leads into a separate personal learning portal", async ({
  page,
}) => {
  await page.goto("/");
  await expect(
    page.getByRole("navigation", { name: "Public navigation" }),
  ).toBeVisible();
  await expect(
    page.getByRole("region", { name: "Learning momentum" }),
  ).toHaveCount(0);
  await expect(page.locator(".portal-navigation")).toHaveCount(0);
  const probabilities = page.getByRole("img", { name: /^Probabilities:/ });
  await expect(probabilities).toHaveAttribute(
    "aria-label",
    /9.0 percent, 24.5 percent, 66.5 percent/,
  );
  await page.getByRole("slider", { name: /Temperature/ }).press("End");
  await expect(probabilities).toHaveAttribute(
    "aria-label",
    /23.0 percent, 32.1 percent, 44.8 percent/,
  );
  await page
    .getByRole("link", { name: "Open learning portal", exact: true })
    .click();
  await expect(page).toHaveURL(/\/learn\/$/);
  await expect(
    page.getByRole("heading", { name: "Your workspace" }),
  ).toBeVisible();
  await expect(
    page.getByRole("navigation", { name: "Main navigation" }),
  ).toBeVisible();
  await expect(page.locator(".public-header")).toHaveCount(0);
  await page.getByRole("link", { name: "Start lesson", exact: true }).click();
  await expect(page).toHaveURL(/\/problems\//);
  await expect(page.getByRole("heading", { level: 1 })).toHaveText(
    "Normalize and Deduplicate Tags",
  );
});

test("the new portal preserves existing completion data across public navigation", async ({
  page,
}) => {
  await page.goto("/learn/");
  await page.evaluate(() =>
    localStorage.setItem("mastery:progress:m02:v1", "complete"),
  );
  await page.reload();
  await expect(page.locator(".dashboard-completion")).toContainText(
    `1 / ${lessonCount} lessons`,
  );
  await page.getByRole("link", { name: "ZeroShot website" }).click();
  await expect(page.locator(".public-header")).toBeVisible();
  await page
    .getByRole("link", { name: "Open learning portal", exact: true })
    .click();
  await expect(page.locator(".dashboard-completion")).toContainText(
    `1 / ${lessonCount} lessons`,
  );
});

test("public and portal layouts fit mobile, with keyboard-operable portal navigation", async ({
  page,
}) => {
  await page.setViewportSize({ width: 390, height: 844 });
  for (const route of ["/", "/about/", "/learn/", "/problems/", "/progress/"]) {
    await page.goto(route);
    expect(
      await page.evaluate(
        () => document.documentElement.scrollWidth <= innerWidth,
      ),
      route,
    ).toBe(true);
    expect(
      await page.evaluate(
        () => getComputedStyle(document.documentElement).colorScheme,
      ),
    ).toBe("dark");
    await expect(page.getByRole("heading", { level: 1 })).toBeVisible();
  }
  const menu = page.getByRole("button", { name: "Toggle learning navigation" });
  await menu.click();
  await expect(menu).toHaveAttribute("aria-expanded", "true");
  const home = page.getByRole("link", { name: "Learning home", exact: true });
  await home.focus();
  await home.press("Escape");
  await expect(menu).toHaveAttribute("aria-expanded", "false");
  await expect(menu).toBeFocused();
  await menu.press("Enter");
  await home.click();
  await expect(page).toHaveURL(/\/learn\/$/);
  await expect(menu).toHaveAttribute("aria-expanded", "false");
});
