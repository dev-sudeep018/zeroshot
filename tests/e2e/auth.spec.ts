import { expect, test } from "@playwright/test";

test("account entry preserves guest access without accepting an external return destination", async ({
  page,
}) => {
  await page.goto("/login/?next=https://external.invalid/");
  await expect(page.locator(".auth-main h1")).toHaveText(
    /Welcome back|Keep learning as a guest/,
  );
  const guest = page.getByRole("link", { name: "Continue as a guest" });
  if (await guest.isVisible()) await guest.click();
  else
    await page
      .getByRole("link", { name: "Open learning portal", exact: true })
      .click();
  await expect(page).toHaveURL(/\/learn\/$/);
  await expect(
    page.getByRole("navigation", { name: "Main navigation" }),
  ).toBeVisible();
});

test("account page explains local work and links back to backups for a guest", async ({
  page,
}) => {
  await page.goto("/account/");
  await expect(
    page.getByRole("heading", { name: "Your account", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("heading", { name: "Your work stays on this device" }),
  ).toBeVisible();
  await expect(
    page.getByText(
      /Signing in does not sync progress or code between devices yet/,
    ),
  ).toBeVisible();
  await page.getByRole("link", { name: "Manage progress and backups" }).click();
  await expect(page).toHaveURL(/\/progress\/$/);
  await expect(page.getByRole("button", { name: /Export/ })).toBeVisible();
});
