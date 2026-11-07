# Authentication

ZeroShot supports optional Firebase email/password accounts: sign-up, sign-in, email verification and resend, password reset, saved sessions, and browser sign-out. Every learning route remains available to guests. The account interface reports successful email requests; it does not claim that a message has reached the recipient.

## Configuration

Copy `apps/web/.env.example` to `apps/web/.env.local` and fill its four `NEXT_PUBLIC_FIREBASE_*` values from the Firebase project's web-app configuration. These values identify the public application; they are bundled into the browser build and are not service credentials. Never put a service-account key, admin credential, or private token in these variables. Missing or malformed configuration leaves account access unavailable and keeps the guest learning links visible.

The existing project is `zeroshot-549bd` on Firebase's Spark plan. This implementation uses email/password authentication and does not require a paid-plan upgrade, phone authentication, Firestore, or a server database. Production setup still needs email/password sign-in enabled and the deployed hostname authorized in Firebase Authentication. Retain the project's abuse protections and configure verification/reset email templates for the final hostname.

Next.js reads public variables during the build. Rebuild the static export after changing them. `NEXT_PUBLIC_FIREBASE_AUTH_EMULATOR_URL` must be absent from production configuration; emulator use is restricted in code to a development build, a `demo-` project, and a loopback application and emulator host.

## Data and session boundaries

Firebase's SDK manages session persistence and token refresh. The application passes passwords directly to Firebase and does not write them to its progress store. Local browser storage still contains learning progress, drafts, and optional momentum data independently of the account. Signing in does not synchronize that data between devices, and signing out does not delete it. People sharing the same browser share its learning data. Export a progress backup before changing devices.

No private learning API or protected user-data service is introduced here. A signed-in UI is not an authorization boundary for a future backend; any future per-user data service needs its own verified token checks and access rules.

## Local verification

Install project dependencies, prepare generated assets, and install Playwright Chromium:

```sh
pnpm install --frozen-lockfile
pnpm setup
pnpm exec playwright install chromium
```

With Firebase CLI `15.6.0`, run from the repository root:

```sh
firebase emulators:exec --config tests/auth/firebase.json --project demo-zeroshot --only auth "node scripts/check-auth-flow.mjs"
```

The verified Windows invocation is:

```powershell
& "$env:APPDATA\npm\firebase.ps1" emulators:exec --config tests/auth/firebase.json --project demo-zeroshot --only auth 'node scripts/check-auth-flow.mjs'
```

The Firebase CLI supplies `FIREBASE_AUTH_EMULATOR_HOST=127.0.0.1:9099`. The harness refuses to run without that exact value. It supplies a synthetic public web configuration for `demo-zeroshot`, starts its own development server at `http://localhost:3002`, and uses the separate `.next-auth` cache. Keep ports 3002 and 9099 free. No production credentials or account are required. Test users use randomly generated `example.invalid` addresses, and emulator accounts are removed during cleanup.

The browser flow covers sign-up; verification status and resend; verification completion; reload persistence; same-session tabs; a separate context remaining a guest; sign-out across tabs; preserved local draft/progress; invalid credentials; account and login password-reset requests; rejection of the old password; and successful sign-in with the new password. It inspects cookies, local/session storage, and IndexedDB for both test passwords and rejects production authentication network calls.

Related checks are `pnpm exec vitest run tests/unit/auth.test.ts` and `pnpm exec playwright test tests/e2e/auth.spec.ts --project=chromium`. Unit checks cover configuration, redirect restrictions, emulator restrictions, and privacy-preserving errors. The regular browser checks cover guest navigation and the local-progress disclosure against the built site.

## Production verification still required

Emulator success does not establish production deployment, email delivery, authorized-domain configuration, or live provider quota behavior. Provider/deployment access was unavailable during this verification. No real account was created or email sent. Before claiming production account readiness, verify the deployed build's project configuration and headers, complete sign-up/verification and reset with an authorized test account, confirm receipt in its inbox, and check reload persistence and sign-out on the actual hostname.
