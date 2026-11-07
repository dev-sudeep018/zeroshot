# Free static deployment

ZeroShot uses two separate Cloudflare Pages projects: the static learning app and the Python runner. Firebase Authentication uses the Spark plan with email/password enabled. Progress and code remain local to each browser; authentication does not add cloud progress storage. See [authentication.md](authentication.md).

## Current status — 7 November 2026

Firebase project `zeroshot-549bd` and its public client configuration were prepared in the earlier setup. Cloudflare account `d8d55480ae574a169aa52c156aba53d5` was identified in that setup. The current Wrangler check reports **not authenticated**. No Pages project names or production URLs have been reserved, no production hostname has been added to Firebase, and no live deployment is claimed.

The user already authorized the free hosting setup and narrow Wrangler OAuth permissions: User Read, Account Read, Pages Write, Background Access. Browser control stopped because it could not reliably determine the browser URL for its policy checks. That tool problem must be resolved before continuing the consent UI; it is not a new request for user authorization. Do not substitute a temporary anonymous preview deployment for the intended production projects.

## Reserve the two origins

With the authorized Wrangler login completed, set `CLOUDFLARE_ACCOUNT_ID` in the shell, run `wrangler whoami`, and use `wrangler pages project list` to inspect existing projects before creating anything. Create two Direct Upload projects with `wrangler pages project create <project-name> --production-branch main`. Choose unique app and runner names and record the exact returned `https://<project>.pages.dev` origins in the private deployment continuation notes. Proposed names are not reserved names.

Use static Pages only. Do not activate Workers billing, Firebase Blaze, paid add-ons, a custom domain purchase, or broad GitHub integration. Direct Upload uses locally built assets; it does not require repository access. [Cloudflare Direct Upload](https://developers.cloudflare.com/pages/get-started/direct-upload/) documents project creation and upload commands.

Add the exact app hostname, without its scheme or path, in Firebase Authentication → Settings → Authorized domains. Keep Email/Password enabled. The runner hostname does not need Firebase authorization. Preview deployment hostnames are intentionally excluded from the runner's parent-origin allowlist.

## Prepare a reviewed release

Run the repository release checks and commit all reviewed source first. No other task may mutate source or generated build directories during packaging. Use the four public Firebase variables from `apps/web/.env.example` in ignored `apps/web/.env.local`; these are client identifiers, not administrative credentials. Never add CLI tokens, service account keys, or emulator configuration to a production package.

In PowerShell, after replacing both placeholders with the reserved names:

```powershell
$env:APP_ORIGIN = 'https://<app-project>.pages.dev'
$env:NEXT_PUBLIC_RUNNER_ORIGIN = 'https://<runner-project>.pages.dev'
$env:CLOUDFLARE_ACCOUNT_ID = 'd8d55480ae574a169aa52c156aba53d5'
node scripts/prepare-deployment.mjs
```

The command refuses a dirty working tree, clears only known generated build directories, and performs a fresh `pnpm build` itself. It verifies that the SHA and source tree stayed unchanged, checks both origins and all four Firebase client settings in the output, and rejects emulator settings. It never accepts a pre-existing build as proof of the current commit.

Output is `work/deployment/<first-12-SHA>/app` and `runner`. Existing output for that SHA is not overwritten. Each directory has an asset hash manifest and the same `release.json`, including the source SHA, build time, Firebase project ID, actual validated lesson/project counts, and both manifest hashes. Draft curriculum under `work/` is not published. The current baseline is 450 lessons plus one project checkpoint; the 2,000-lesson target must not be reported as complete.

Packaging enforces the Pages Free ceilings of 20,000 files per project and 25 MiB per asset. These limits must still pass as the curriculum grows; increasing the target count is not permission to enable billing. [Cloudflare Pages limits](https://developers.cloudflare.com/pages/platform/limits/) defines the provider ceilings.

## Upload and verify

Upload the runner first, then the app, from their exact packaged directories:

```powershell
$revision = git rev-parse HEAD
$releaseDirectory = "work/deployment/$($revision.Substring(0, 12))"
wrangler pages deploy "$releaseDirectory/runner" --project-name <runner-project> --branch main --commit-hash $revision
wrangler pages deploy "$releaseDirectory/app" --project-name <app-project> --branch main --commit-hash $revision
node scripts/verify-deployment.mjs $env:APP_ORIGIN $env:NEXT_PUBLIC_RUNNER_ORIGIN $revision
node scripts/verify-deployment-browser.mjs $env:APP_ORIGIN $env:NEXT_PUBLIC_RUNNER_ORIGIN $revision
```

Use the stable project origins for verification, not the unique preview URL returned by upload. The runner only accepts the configured app origin. The HTTP check verifies matching release metadata, manifest hashes, representative runtime bytes, page availability, restrictive runner headers, absence of CORS/cookies, unknown-file rejection and method rejection. A provider response that differs from the expected 405 for POST is a release failure to investigate, not a reason to weaken the check silently.

The browser script runs a real NumPy lesson, probes parent/storage/network isolation, checks forged completion rejection, exercises guest entry, and verifies a real Firebase invalid-credential response using a unique nonexistent address. It never creates an account or sends email. Screenshots and a precise report are saved under `work/deployment/`. Those checks do not establish successful account creation or mail delivery.

To complete live authentication verification, use an owned test mailbox: create an account, inspect actual verification email receipt, complete its link, sign out and sign in, reload to confirm session persistence, request and receive a reset email, complete it, confirm the old password fails and the new password succeeds. Record only redacted outcomes and timestamps. Do not save passwords, action links, ID tokens or OAuth credentials in evidence. Emulator tests are necessary implementation evidence but do not replace these production checks.

## Updating or recovering

Preserve the previous verified package and both deployment IDs. App and runner releases must be compatible and share the same SHA; an interrupted upload is not a completed release. If a new runner becomes incompatible with the old app, restore the previous runner from its preserved package. Roll back both projects together when restoring a previous release, then rerun the HTTP and browser checks. Never claim production readiness from an upload success alone.
