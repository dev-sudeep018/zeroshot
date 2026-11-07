import assert from "node:assert/strict";
import { createHash } from "node:crypto";
const [appOrigin, runnerOrigin, revision] = process.argv.slice(2);
if (!appOrigin || !runnerOrigin || !revision)
  throw new Error(
    "Usage: node scripts/verify-deployment.mjs <app-origin> <runner-origin> <full-git-sha>",
  );
for (const origin of [appOrigin, runnerOrigin])
  assert.match(origin, /^https:\/\/[a-z0-9][a-z0-9-]*\.pages\.dev$/);
assert.match(revision, /^[a-f0-9]{40}$/);
assert.notEqual(appOrigin, runnerOrigin);
const sha256 = (bytes) => createHash("sha256").update(bytes).digest("hex");
const requests = [];
const manifests = {};
async function request(origin, route, init) {
  const url = new URL(route, origin);
  const response = await fetch(url, {
    redirect: "manual",
    signal: AbortSignal.timeout(60000),
    ...init,
  });
  requests.push({ url: url.href, status: response.status });
  return response;
}
let appRelease;
for (const origin of [appOrigin, runnerOrigin]) {
  const release = await request(origin, "/release.json");
  assert.equal(release.status, 200);
  const value = await release.json();
  assert.equal(value.schemaVersion, 1);
  assert.equal(value.revision, revision);
  assert.equal(value.appOrigin, appOrigin);
  assert.equal(value.runnerOrigin, runnerOrigin);
  if (appRelease) assert.deepEqual(value, appRelease);
  else appRelease = value;
  assert.ok(value.content.lessons > 0);
  assert.equal(
    value.content.lessons + value.content.projects,
    value.content.packages,
  );
  assert.ok(Date.parse(value.buildStartedAt) <= Date.parse(value.createdAt));
  const name = origin === appOrigin ? "app" : "runner";
  const manifestResponse = await request(origin, "/asset-manifest.json");
  assert.equal(manifestResponse.status, 200);
  const bytes = Buffer.from(await manifestResponse.arrayBuffer());
  assert.equal(sha256(bytes), value.artifacts[name].manifestSha256);
  manifests[name] = JSON.parse(bytes.toString("utf8"));
  assert.equal(
    Object.keys(manifests[name]).length + 2,
    value.artifacts[name].files,
  );
  assert.ok(value.artifacts[name].files <= 20000);
}
for (const route of [
  "/",
  "/learn/",
  "/problems/",
  "/paths/",
  "/progress/",
  "/account/",
  "/login/",
  "/about/",
  "/problems/stable-softmax/",
]) {
  const response = await request(appOrigin, route);
  assert.equal(response.status, 200, `${route}: route unavailable`);
  assert.match(response.headers.get("content-type") ?? "", /text\/html/);
  assert.match(await response.text(), /ZeroShot/);
  const csp = response.headers.get("content-security-policy") ?? "";
  assert.ok(csp.includes("frame-ancestors 'none'"));
  assert.equal(response.headers.get("x-content-type-options"), "nosniff");
}
for (const route of [
  "/",
  "/bridge.js",
  "/worker.js",
  "/runtime/pyodide.asm.wasm",
  "/generated/m02-v1.py",
]) {
  const response = await request(runnerOrigin, route);
  assert.equal(response.status, 200, `${route}: runner asset unavailable`);
  const csp = response.headers.get("content-security-policy") ?? "";
  for (const directive of [
    "default-src 'none'",
    "connect-src 'self'",
    "worker-src 'self'",
    `frame-ancestors ${appOrigin}`,
  ])
    assert.ok(csp.includes(directive), `${route}: missing ${directive}`);
  assert.ok(!csp.includes("'unsafe-eval'"), `${route}: unsafe eval permitted`);
  assert.equal(response.headers.get("x-content-type-options"), "nosniff");
  assert.equal(
    response.headers.get("cross-origin-resource-policy"),
    "same-origin",
  );
  assert.equal(response.headers.get("access-control-allow-origin"), null);
  assert.equal(response.headers.get("set-cookie"), null);
  const bytes = Buffer.from(await response.arrayBuffer());
  const asset = manifests.runner[route === "/" ? "index.html" : route.slice(1)];
  assert.ok(asset, `${route}: missing asset provenance`);
  assert.equal(bytes.length, asset.bytes);
  assert.equal(
    sha256(bytes),
    asset.sha256,
    `${route}: deployed bytes differ from release`,
  );
}
assert.equal((await request(runnerOrigin, "/does-not-exist")).status, 404);
assert.equal(
  (await request(runnerOrigin, "/", { method: "POST", body: "probe" })).status,
  405,
);
const bridge = await request(runnerOrigin, "/bridge.js");
const source = await bridge.text();
assert.ok(source.includes(appOrigin));
assert.ok(!source.includes("http://localhost:3000"));
console.log(
  JSON.stringify(
    {
      revision,
      status: "passed",
      content: appRelease.content,
      firebaseProjectId: appRelease.firebaseProjectId,
      requests,
    },
    null,
    2,
  ),
);
console.log(
  "HTTP checks passed. Still run live browser execution and isolation tests; HTTP checks alone are not a release gate.",
);
