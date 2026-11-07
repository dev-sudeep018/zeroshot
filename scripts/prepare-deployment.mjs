import {
  cp,
  mkdir,
  readdir,
  readFile,
  rm,
  stat,
  writeFile,
} from "node:fs/promises";
import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("../", import.meta.url));
if (process.argv.length > 2)
  throw new Error(
    "This command always builds fresh; it accepts no skip-build option.",
  );
const appOrigin = process.env.APP_ORIGIN;
const runnerOrigin = process.env.NEXT_PUBLIC_RUNNER_ORIGIN;
const pagesOrigin = /^https:\/\/[a-z0-9][a-z0-9-]*\.pages\.dev$/;
if (
  !pagesOrigin.test(appOrigin ?? "") ||
  !pagesOrigin.test(runnerOrigin ?? "") ||
  appOrigin === runnerOrigin
) {
  throw new Error(
    "Set APP_ORIGIN and NEXT_PUBLIC_RUNNER_ORIGIN to two different production https://<project>.pages.dev origins before building and packaging.",
  );
}
function git(...args) {
  return execFileSync("git", args, { cwd: root, encoding: "utf8" }).trim();
}
function assertClean(revision) {
  if (git("status", "--porcelain"))
    throw new Error("Commit the reviewed source before packaging a release.");
  if (git("rev-parse", "HEAD") !== revision)
    throw new Error("Source revision changed during release preparation.");
}
const revision = git("rev-parse", "HEAD");
assertClean(revision);
const publicEnv = {};
// Match Next's production precedence, without printing any environment contents.
for (const name of [
  ".env",
  ".env.production",
  ".env.local",
  ".env.production.local",
]) {
  try {
    const source = await readFile(path.join(root, "apps/web", name), "utf8");
    for (const line of source.split(/\r?\n/)) {
      const match = line.match(
        /^\s*(NEXT_PUBLIC_FIREBASE_[A-Z_]+)\s*=\s*(.*?)\s*$/,
      );
      if (match) publicEnv[match[1]] = match[2].replace(/^(['"])(.*)\1$/, "$2");
    }
  } catch (error) {
    if (error.code !== "ENOENT") throw error;
  }
}
for (const [key, value] of Object.entries(process.env))
  if (key.startsWith("NEXT_PUBLIC_FIREBASE_")) publicEnv[key] = value;
for (const name of ["API_KEY", "AUTH_DOMAIN", "PROJECT_ID", "APP_ID"])
  if (!publicEnv[`NEXT_PUBLIC_FIREBASE_${name}`])
    throw new Error(`Missing production Firebase setting: ${name}`);
if (
  publicEnv.NEXT_PUBLIC_FIREBASE_AUTH_EMULATOR_URL ||
  publicEnv.NEXT_PUBLIC_FIREBASE_PROJECT_ID.startsWith("demo-") ||
  process.env.ZEROSHOT_AUTH_TEST
)
  throw new Error(
    "Production packaging cannot use the authentication emulator.",
  );
if (
  publicEnv.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN !==
  `${publicEnv.NEXT_PUBLIC_FIREBASE_PROJECT_ID}.firebaseapp.com`
)
  throw new Error("Firebase project and authentication domain do not match.");
// Remove only these known generated directories. Resolve each path before deletion.
for (const relative of [
  "apps/web/.next",
  "apps/web/out",
  "apps/web/src/generated",
  "apps/runner/src/generated",
  "apps/runner/public/generated",
]) {
  const directory = path.resolve(root, relative);
  if (!directory.startsWith(path.resolve(root) + path.sep))
    throw new Error("Generated directory escaped the repository.");
  await rm(directory, { recursive: true, force: true });
}
const buildStartedAt = new Date().toISOString();
console.log(
  `Building reviewed revision ${revision} for the two production origins.`,
);
execFileSync(
  process.platform === "win32" ? "cmd.exe" : "pnpm",
  process.platform === "win32" ? ["/d", "/s", "/c", "pnpm build"] : ["build"],
  {
    cwd: root,
    stdio: "inherit",
    env: {
      ...process.env,
      ...publicEnv,
      NODE_ENV: "production",
      NEXT_TELEMETRY_DISABLED: "1",
    },
  },
);
assertClean(revision);
const bridge = await readFile(
  path.join(root, "apps/runner/public/bridge.js"),
  "utf8",
);
if (!bridge.includes(appOrigin) || bridge.includes("http://localhost:3000")) {
  throw new Error(
    "Runner was not built for APP_ORIGIN. Rebuild with the production environment.",
  );
}
async function files(directory) {
  const result = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const file = path.join(directory, entry.name);
    if (entry.isDirectory()) result.push(...(await files(file)));
    else if (entry.isFile()) result.push(file);
    else throw new Error(`Unexpected non-file asset: ${file}`);
  }
  return result;
}
const webSource = path.join(root, "apps/web/out");
const webFiles = await files(webSource);
let runnerConfigured = false;
const firebaseValues = new Set(
  ["API_KEY", "AUTH_DOMAIN", "PROJECT_ID", "APP_ID"].map(
    (name) => publicEnv[`NEXT_PUBLIC_FIREBASE_${name}`],
  ),
);
for (const file of webFiles.filter((file) => file.endsWith(".js"))) {
  const source = await readFile(file, "utf8");
  if (source.includes(runnerOrigin)) runnerConfigured = true;
  for (const value of firebaseValues)
    if (source.includes(value)) firebaseValues.delete(value);
}
if (firebaseValues.size)
  throw new Error(
    "Production Firebase settings are absent from the built client.",
  );
if (!runnerConfigured)
  throw new Error(
    "Static app does not contain the production runner origin. Rebuild it first.",
  );
const deploymentRoot = path.join(
  root,
  "work/deployment",
  revision.slice(0, 12),
);
// Refuse to overlay a previous package: stale files must never survive a release.
await mkdir(path.dirname(deploymentRoot), { recursive: true });
await mkdir(deploymentRoot, { recursive: false });
const app = path.join(deploymentRoot, "app");
const runner = path.join(deploymentRoot, "runner");
await cp(webSource, app, { recursive: true });
await cp(path.join(root, "apps/runner/public"), runner, {
  recursive: true,
  filter: (source) =>
    !path.basename(source).startsWith(".") && !source.endsWith(".map"),
});
const runnerCsp = `default-src 'none'; script-src 'self' 'wasm-unsafe-eval'; worker-src 'self'; connect-src 'self'; img-src 'none'; style-src 'none'; font-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors ${appOrigin}; object-src 'none'`;
await writeFile(
  path.join(runner, "_headers"),
  `/*\n  Content-Security-Policy: ${runnerCsp}\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: no-referrer\n  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(), usb=()\n  Cross-Origin-Resource-Policy: same-origin\n  Cache-Control: no-store\n/runtime/*\n  Cache-Control: public, max-age=3600\n`,
);
await writeFile(
  path.join(runner, "404.html"),
  '<!doctype html><html lang="en"><meta charset="utf-8"><title>Not found</title><p>This runner file does not exist.</p></html>\n',
);
await writeFile(
  path.join(app, "_headers"),
  `/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(), usb=()\n  Content-Security-Policy: frame-ancestors 'none'; object-src 'none'; base-uri 'self'\n`,
);
const release = {
  schemaVersion: 1,
  revision,
  buildStartedAt,
  createdAt: new Date().toISOString(),
  appOrigin,
  runnerOrigin,
  firebaseProjectId: publicEnv.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  content: {},
  artifacts: {},
};
const catalog = JSON.parse(
  await readFile(
    path.join(root, "apps/web/src/generated/catalog.json"),
    "utf8",
  ),
);
if (catalog.some((item) => item.status !== "validated"))
  throw new Error("Unvalidated content in the production catalog.");
release.content = {
  lessons: catalog.filter((item) => item.kind === "lesson").length,
  projects: catalog.filter((item) => item.kind === "project").length,
  packages: catalog.length,
};
const sha256 = (bytes) => createHash("sha256").update(bytes).digest("hex");
for (const [name, directory] of [
  ["app", app],
  ["runner", runner],
]) {
  const assets = (await files(directory)).sort();
  if (assets.length + 2 > 20_000)
    throw new Error(`${name}: exceeds Pages Free's 20,000-file limit.`);
  for (const file of assets) {
    if ((await stat(file)).size > 25 * 1024 * 1024)
      throw new Error(`Pages asset exceeds 25 MiB: ${file}`);
  }
  const manifest = {};
  for (const file of assets) {
    if (
      /\.(?:map|env)$/.test(file) ||
      path.basename(file).startsWith(".") ||
      path.basename(file) === "_worker.js"
    )
      throw new Error(`Unexpected deployment asset: ${file}`);
    const bytes = await readFile(file);
    manifest[path.relative(directory, file).split(path.sep).join("/")] = {
      bytes: bytes.length,
      sha256: sha256(bytes),
    };
  }
  const serialized = JSON.stringify(manifest, null, 2) + "\n";
  await writeFile(path.join(directory, "asset-manifest.json"), serialized);
  release.artifacts[name] = {
    files: assets.length + 2,
    manifestSha256: sha256(serialized),
  };
  console.log(`${name}: ${assets.length + 2} files ready at ${directory}`);
}
assertClean(revision);
for (const directory of [app, runner])
  await writeFile(
    path.join(directory, "release.json"),
    JSON.stringify(release, null, 2) + "\n",
  );
console.log(
  `Prepared ${revision}; upload the runner first, then the app. Verify both live origins before announcing release.`,
);
