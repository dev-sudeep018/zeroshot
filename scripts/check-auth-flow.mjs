import assert from "node:assert/strict";
import { randomUUID } from "node:crypto";
import { spawn } from "node:child_process";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { chromium } from "@playwright/test";

const root = fileURLToPath(new URL("../", import.meta.url));
const require = createRequire(path.join(root, "apps/web/package.json"));
const emulator = "http://127.0.0.1:9099";
const application = "http://localhost:3002";
const project = "demo-zeroshot";
const apiKey = `AIza${"a".repeat(35)}`;
const email = `learner-${randomUUID()}@example.invalid`;
const password = `Initial-${randomUUID()}!`;
const nextPassword = `Reset-${randomUUID()}!`;
const savedDraft = "# Local draft preserved across account changes\nprint(1)";
const savedProgress = JSON.stringify({
  "m01:v1": { updatedAt: 1, completed: true, attempts: 1 },
});
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
if (process.env.FIREBASE_AUTH_EMULATOR_HOST !== "127.0.0.1:9099")
  throw new Error(
    "Run via Firebase emulators:exec; this test must never use production accounts.",
  );

const child = spawn(
  process.execPath,
  [
    require.resolve("next/dist/bin/next"),
    "dev",
    "--webpack",
    "--hostname",
    "localhost",
    "--port",
    "3002",
  ],
  {
    cwd: path.join(root, "apps/web"),
    env: {
      ...process.env,
      NODE_ENV: "development",
      ZEROSHOT_AUTH_TEST: "1",
      NEXT_PUBLIC_FIREBASE_API_KEY: apiKey,
      NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN: `${project}.firebaseapp.com`,
      NEXT_PUBLIC_FIREBASE_PROJECT_ID: project,
      NEXT_PUBLIC_FIREBASE_APP_ID: "1:123456789:web:abcdef123456",
      NEXT_PUBLIC_FIREBASE_AUTH_EMULATOR_URL: emulator,
    },
    stdio: ["ignore", "pipe", "pipe"],
    windowsHide: true,
  },
);
let logs = "";
for (const stream of [child.stdout, child.stderr])
  stream.on("data", (chunk) => {
    logs = (logs + chunk.toString()).slice(-12000);
  });
let browser;
const expectVisible = async (locator) => {
  await locator.waitFor({ state: "visible", timeout: 30000 });
};
async function emulatorPost(method, body) {
  const response = await fetch(
    `${emulator}/identitytoolkit.googleapis.com/v1/${method}?key=${apiKey}`,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    },
  );
  const result = await response.json();
  assert.equal(response.ok, true, `Emulator operation ${method} failed`);
  return result;
}
async function outOfBandCode(requestType) {
  const response = await fetch(
    `${emulator}/emulator/v1/projects/${project}/oobCodes`,
  );
  assert.equal(response.ok, true);
  const { oobCodes } = await response.json();
  const code = oobCodes
    .filter(
      (entry) => entry.email === email && entry.requestType === requestType,
    )
    .at(-1);
  assert.ok(code?.oobCode, `Missing emulator ${requestType} message`);
  return code.oobCode;
}

try {
  const deadline = Date.now() + 180000;
  let ready = false;
  while (Date.now() < deadline) {
    if (child.exitCode !== null)
      throw new Error(`Auth test server exited: ${logs}`);
    try {
      if ((await fetch(`${application}/login/`)).ok) {
        ready = true;
        break;
      }
    } catch {
      /* Waiting for the isolated dev server. */
    }
    await sleep(1000);
  }
  assert.ok(ready, `Auth test server did not start: ${logs}`);
  browser = await chromium.launch();
  const context = await browser.newContext();
  const externalAuth = [];
  const isolateAuth = async (route) => {
    const url = new URL(route.request().url());
    if (
      ["identitytoolkit.googleapis.com", "securetoken.googleapis.com"].includes(
        url.hostname,
      )
    ) {
      externalAuth.push(url.origin);
      await route.abort();
    } else await route.continue();
  };
  await context.route("**/*", isolateAuth);
  const page = await context.newPage();
  await page.goto(`${application}/login/?mode=signup`);
  await expectVisible(
    page.getByRole("heading", { name: "Create your account", exact: true }),
  );
  await page.evaluate(
    ({ draft, progress }) => {
      localStorage.setItem("mastery:draft:m01:v1", draft);
      localStorage.setItem("mastery:learning:v1", progress);
    },
    { draft: savedDraft, progress: savedProgress },
  );
  await page.getByLabel("Email address", { exact: true }).fill(email);
  await page.getByLabel("Password", { exact: true }).fill(password);
  await page.locator(".auth-submit").click();
  await expectVisible(page.getByRole("heading", { name: "You’re signed in" }));
  await expectVisible(
    page.getByText(/A verification email has been requested/),
  );
  await page.getByRole("link", { name: "Manage your account" }).click();
  await expectVisible(
    page.getByText("Email verification needed", { exact: true }),
  );
  await page.getByRole("button", { name: "I’ve verified my email" }).click();
  await expectVisible(page.getByText(/Your email hasn't been verified yet/));
  await page.getByRole("button", { name: "Resend verification email" }).click();
  await expectVisible(
    page.getByText(/A verification email has been requested/),
  );
  await emulatorPost("accounts:update", {
    oobCode: await outOfBandCode("VERIFY_EMAIL"),
  });
  await page.getByRole("button", { name: "I’ve verified my email" }).click();
  await expectVisible(page.getByText("Email verified", { exact: true }));
  await page.reload();
  await expectVisible(page.getByText("Email verified", { exact: true }));
  await page.getByRole("button", { name: "Request password reset" }).click();
  await expectVisible(
    page.getByText(/A password reset link has been requested/),
  );
  const second = await context.newPage();
  await second.goto(`${application}/account/`);
  await expectVisible(second.getByText("Email verified", { exact: true }));
  const privateContext = await browser.newContext();
  await privateContext.route("**/*", isolateAuth);
  const guest = await privateContext.newPage();
  await guest.goto(`${application}/account/`);
  await expectVisible(
    guest.getByRole("heading", { name: "You’re learning as a guest" }),
  );
  await privateContext.close();
  await page.getByRole("button", { name: "Sign out", exact: true }).click();
  await expectVisible(
    page.getByRole("heading", { name: "You’re learning as a guest" }),
  );
  await expectVisible(
    second.getByRole("heading", { name: "You’re learning as a guest" }),
  );
  assert.deepEqual(
    await page.evaluate(() => ({
      draft: localStorage.getItem("mastery:draft:m01:v1"),
      progress: localStorage.getItem("mastery:learning:v1"),
    })),
    { draft: savedDraft, progress: savedProgress },
    "Signing out changed browser-local learning data",
  );
  await page.goto(`${application}/login/?next=/account/`);
  await page.getByLabel("Email address", { exact: true }).fill(email);
  await page.getByLabel("Password", { exact: true }).fill("wrong-password");
  await page.locator(".auth-submit").click();
  const signInError = page.locator('.auth-notice[role="alert"]');
  await expectVisible(signInError);
  assert.match(await signInError.innerText(), /couldn't sign you in/);
  await page.getByRole("button", { name: "Forgot your password?" }).click();
  await page.locator(".auth-submit").click();
  await expectVisible(page.getByText(/If an account uses that email/));
  await emulatorPost("accounts:resetPassword", {
    oobCode: await outOfBandCode("PASSWORD_RESET"),
    newPassword: nextPassword,
  });
  await page.getByRole("button", { name: "Back to sign in" }).click();
  await page.getByLabel("Password", { exact: true }).fill(password);
  await page.locator(".auth-submit").click();
  await expectVisible(signInError);
  assert.match(await signInError.innerText(), /couldn't sign you in/);
  await page.getByLabel("Password", { exact: true }).fill(nextPassword);
  await page.locator(".auth-submit").click();
  await page.waitForURL(`${application}/account/`, { timeout: 30000 });
  await expectVisible(page.getByText("Email verified", { exact: true }));
  const storage = JSON.stringify({
    persistent: await context.storageState({ indexedDB: true }),
    session: await page.evaluate(() => ({ ...sessionStorage })),
  });
  assert.equal(
    storage.includes(password),
    false,
    "Initial password leaked to browser storage",
  );
  assert.equal(
    storage.includes(nextPassword),
    false,
    "Reset password leaked to browser storage",
  );
  assert.deepEqual(
    externalAuth,
    [],
    "Emulator flow attempted a production authentication request",
  );
  await context.close();
  console.log(
    "Auth flow passed: signup, verification and resend, reload persistence, private-context isolation, cross-tab sign-out, preserved local work, invalid credentials, account and login password reset, old-password rejection and new-password sign-in. No passwords in cookies, web storage or IndexedDB. No production auth requests.",
  );
} catch (error) {
  if (browser) {
    const page = browser.contexts()[0]?.pages()[0];
    if (page)
      console.error(
        (
          await page
            .locator("main")
            .innerText()
            .catch(() => "")
        ).slice(0, 3000),
      );
  }
  throw error;
} finally {
  await browser?.close();
  await fetch(`${emulator}/emulator/v1/projects/${project}/accounts`, {
    method: "DELETE",
  }).catch(() => {});
  child.kill();
}
