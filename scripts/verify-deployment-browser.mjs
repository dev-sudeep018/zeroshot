import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { randomUUID } from "node:crypto";
import { chromium, expect } from "@playwright/test";

const [appOrigin, runnerOrigin, revision] = process.argv.slice(2);
for (const origin of [appOrigin, runnerOrigin])
  assert.match(origin ?? "", /^https:\/\/[a-z0-9][a-z0-9-]*\.pages\.dev$/);
assert.notEqual(appOrigin, runnerOrigin);
assert.match(revision ?? "", /^[a-f0-9]{40}$/);
const root = fileURLToPath(new URL("../", import.meta.url));
const evidence = path.join(
  root,
  "work/deployment",
  `${revision.slice(0, 12)}-browser-${Date.now()}`,
);
await mkdir(evidence, { recursive: true });
const reference = execFileSync(
  "git",
  ["show", `${revision}:content/problems/m02-stable-softmax/solution.py`],
  { cwd: root, encoding: "utf8" },
);
const checks = [];
const browser = await chromium.launch();
try {
  const context = await browser.newContext({
    viewport: { width: 1440, height: 1000 },
  });
  const page = await context.newPage();
  for (const origin of [appOrigin, runnerOrigin]) {
    const response = await context.request.get(`${origin}/release.json`);
    assert.equal(response.status(), 200);
    assert.equal((await response.json()).revision, revision);
  }
  // This request cannot create an account or send mail; no real credentials are used.
  await page.goto(`${appOrigin}/login/?next=https://external.invalid/`);
  await expect(
    page.getByRole("heading", { name: "Welcome back", exact: true }),
  ).toBeVisible();
  await page
    .getByLabel("Email address", { exact: true })
    .fill(`deployment-${randomUUID()}@example.invalid`);
  await page
    .getByLabel("Password", { exact: true })
    .fill(`Invalid-${randomUUID()}!`);
  const responsePromise = page.waitForResponse((response) => {
    const url = new URL(response.url());
    return (
      url.hostname === "identitytoolkit.googleapis.com" &&
      url.pathname.endsWith("/accounts:signInWithPassword")
    );
  });
  await page
    .locator("form")
    .getByRole("button", { name: "Sign in", exact: true })
    .click();
  const response = await responsePromise;
  assert.equal(response.status(), 400);
  const failure = (await response.json()).error?.message;
  assert.ok(
    [
      "INVALID_LOGIN_CREDENTIALS",
      "EMAIL_NOT_FOUND",
      "INVALID_PASSWORD",
    ].includes(failure),
    "Firebase must reject credentials, not project configuration",
  );
  await expect(page.getByRole("alert")).toContainText(
    "We couldn't sign you in with those details",
  );
  checks.push("Production Firebase SDK and invalid-credential response");
  await page
    .getByRole("link", { name: "Continue as a guest", exact: true })
    .click();
  await expect(page).toHaveURL(`${appOrigin}/learn/`);
  checks.push("Guest entry and external return destination rejected");
  await page.screenshot({
    path: path.join(evidence, "portal.png"),
    fullPage: true,
  });

  const probe =
    `import js\nfrom pyodide.ffi import JsException\nfor url in [${JSON.stringify(appOrigin + "/")}, "https://example.com/"]:\n    try:\n        xhr = js.XMLHttpRequest.new()\n        xhr.open("GET", url, False)\n        xhr.send(None)\n        raise AssertionError("NETWORK WAS NOT BLOCKED")\n    except JsException:\n        print("NETWORK_BLOCKED")\nassert not hasattr(js.globalThis, "document")\nassert not hasattr(js.globalThis, "localStorage")\nprint("NO_APP_STORAGE")\n` +
    reference;
  await context.addInitScript(
    ({ origin, code }) => {
      if (location.origin === origin)
        localStorage.setItem(
          "mastery:draft:m02:v1",
          JSON.stringify({ version: 1, code }),
        );
    },
    { origin: appOrigin, code: probe },
  );
  await page.goto(`${appOrigin}/problems/stable-softmax/`);
  const run = page.getByRole("button", { name: "Check solution", exact: true });
  await expect(run).toBeEnabled({ timeout: 30000 });
  const frame = page
    .frames()
    .find((candidate) => candidate.url().startsWith(runnerOrigin + "/"));
  assert.ok(frame, "Separate production runner frame is missing");
  assert.equal(
    await frame.evaluate(() => {
      try {
        return parent.document.cookie;
      } catch {
        return "BLOCKED";
      }
    }),
    "BLOCKED",
  );
  await page.evaluate(() =>
    window.postMessage(
      { kind: "result", protocol: 1, status: "passed", tests: [] },
      "*",
    ),
  );
  await expect(page.getByText("All checks passed. Nicely done.")).toHaveCount(
    0,
  );
  await run.click();
  await expect(page.getByText("All checks passed. Nicely done.")).toBeVisible({
    timeout: 90000,
  });
  await expect(page.locator(".console-output")).toContainText(
    "NETWORK_BLOCKED",
  );
  await expect(page.locator(".console-output")).toContainText("NO_APP_STORAGE");
  checks.push(
    "Real Python/NumPy reference passed on separate production runner",
    "Parent document, external network, application network and storage isolated",
    "Forged completion message ignored",
  );
  await page.screenshot({
    path: path.join(evidence, "runner.png"),
    fullPage: true,
  });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(appOrigin);
  assert.ok(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= innerWidth + 1,
    ),
    "Mobile page overflows horizontally",
  );
  await page.screenshot({
    path: path.join(evidence, "mobile.png"),
    fullPage: true,
  });
  checks.push("Mobile homepage has no horizontal overflow");
  const report = {
    revision,
    appOrigin,
    runnerOrigin,
    status: "passed",
    checks,
    unverified: [
      "Real account creation and successful sign-in",
      "Verification email receipt and link completion",
      "Password reset email receipt and link completion",
    ],
  };
  await writeFile(
    path.join(evidence, "report.json"),
    JSON.stringify(report, null, 2) + "\n",
  );
  console.log(JSON.stringify(report, null, 2));
  console.log(`Evidence saved at ${evidence}`);
} finally {
  await browser.close();
}
