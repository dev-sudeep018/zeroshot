import type { Auth } from "firebase/auth";
import { localAuthEmulator, readAuthConfig } from "./auth";

// These identify the public Firebase project; no server credentials belong here.
export const firebaseConfig = readAuthConfig({
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
});

let authPromise: Promise<Auth | null> | undefined;

export function getFirebaseAuth(): Promise<Auth | null> {
  if (typeof window === "undefined" || !firebaseConfig)
    return Promise.resolve(null);
  if (!authPromise) {
    authPromise = Promise.all([import("firebase/app"), import("firebase/auth")])
      .then(([appSdk, authSdk]) => {
        const name = "zeroshot-web";
        const app =
          appSdk.getApps().find((entry) => entry.name === name) ??
          appSdk.initializeApp(firebaseConfig, name);
        // Firebase manages persistence and credential refresh. The application
        // never writes passwords or tokens to its learning-progress storage.
        const auth = authSdk.getAuth(app);
        const emulator = localAuthEmulator(
          process.env.NEXT_PUBLIC_FIREBASE_AUTH_EMULATOR_URL,
          window.location.hostname,
          process.env.NODE_ENV,
          firebaseConfig.projectId,
        );
        if (emulator)
          authSdk.connectAuthEmulator(auth, emulator, {
            disableWarnings: true,
          });
        auth.useDeviceLanguage();
        return auth;
      })
      .catch((error: unknown) => {
        authPromise = undefined;
        throw error;
      });
  }
  return authPromise;
}
