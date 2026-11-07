"use client";
import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
} from "react";
import type { User } from "firebase/auth";
import { getFirebaseAuth } from "@/lib/firebase";
import { authErrorCode } from "@/lib/auth";

export type AccountUser = {
  uid: string;
  email: string | null;
  emailVerified: boolean;
};
type AuthStatus = "loading" | "ready" | "unavailable" | "error";
type AuthContextValue = {
  status: AuthStatus;
  user: AccountUser | null;
  signIn: (email: string, password: string) => Promise<void>;
  signUp: (
    email: string,
    password: string,
  ) => Promise<{ verificationSent: boolean }>;
  signOut: () => Promise<void>;
  resetPassword: (email: string) => Promise<void>;
  sendVerification: () => Promise<void>;
  refreshUser: () => Promise<boolean>;
};
const AuthContext = createContext<AuthContextValue | null>(null);
const profile = (user: User | null): AccountUser | null =>
  user
    ? { uid: user.uid, email: user.email, emailVerified: user.emailVerified }
    : null;

async function requireAuth() {
  const auth = await getFirebaseAuth();
  if (!auth)
    throw Object.assign(new Error("Authentication unavailable"), {
      code: "auth/configuration-not-found",
    });
  return auth;
}
const actionSettings = (path: string) => ({
  url: new URL(path, window.location.origin).href,
  handleCodeInApp: false,
});

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [status, setStatus] = useState<AuthStatus>("loading");
  const [user, setUser] = useState<AccountUser | null>(null);
  useEffect(() => {
    let active = true;
    let unsubscribe: (() => void) | undefined;
    void getFirebaseAuth()
      .then(async (auth) => {
        if (!active) return;
        if (!auth) {
          setStatus("unavailable");
          return;
        }
        const { onAuthStateChanged } = await import("firebase/auth");
        if (!active) return;
        unsubscribe = onAuthStateChanged(
          auth,
          (nextUser) => {
            setUser(profile(nextUser));
            setStatus("ready");
          },
          () => {
            setUser(null);
            setStatus("error");
          },
        );
      })
      .catch(() => {
        if (active) setStatus("error");
      });
    return () => {
      active = false;
      unsubscribe?.();
    };
  }, []);

  const signIn = useCallback(async (email: string, password: string) => {
    const auth = await requireAuth();
    const { signInWithEmailAndPassword } = await import("firebase/auth");
    const result = await signInWithEmailAndPassword(
      auth,
      email.trim(),
      password,
    );
    setUser(profile(result.user));
  }, []);
  const signUp = useCallback(async (email: string, password: string) => {
    const auth = await requireAuth();
    const { createUserWithEmailAndPassword, sendEmailVerification } =
      await import("firebase/auth");
    const result = await createUserWithEmailAndPassword(
      auth,
      email.trim(),
      password,
    );
    setUser(profile(result.user));
    try {
      await sendEmailVerification(result.user, actionSettings("/account/"));
      return { verificationSent: true };
    } catch {
      // Account creation succeeded even if email delivery could not be requested.
      // Keep the real signed-in state and let Account offer a retry.
      return { verificationSent: false };
    }
  }, []);
  const signOut = useCallback(async () => {
    const auth = await requireAuth();
    const sdk = await import("firebase/auth");
    await sdk.signOut(auth);
    setUser(null);
  }, []);
  const resetPassword = useCallback(async (email: string) => {
    const auth = await requireAuth();
    const { sendPasswordResetEmail } = await import("firebase/auth");
    try {
      await sendPasswordResetEmail(
        auth,
        email.trim(),
        actionSettings("/login/"),
      );
    } catch (error) {
      // Match the provider's enumeration protection for older configurations.
      if (authErrorCode(error) !== "auth/user-not-found") throw error;
    }
  }, []);
  const sendVerification = useCallback(async () => {
    const auth = await requireAuth();
    if (!auth.currentUser)
      throw Object.assign(new Error("Session required"), {
        code: "auth/user-token-expired",
      });
    const { sendEmailVerification } = await import("firebase/auth");
    await sendEmailVerification(auth.currentUser, actionSettings("/account/"));
  }, []);
  const refreshUser = useCallback(async () => {
    const auth = await requireAuth();
    if (!auth.currentUser) {
      setUser(null);
      return false;
    }
    const { reload } = await import("firebase/auth");
    await reload(auth.currentUser);
    setUser(profile(auth.currentUser));
    return auth.currentUser?.emailVerified ?? false;
  }, []);
  const value = useMemo(
    () => ({
      status,
      user,
      signIn,
      signUp,
      signOut,
      resetPassword,
      sendVerification,
      refreshUser,
    }),
    [
      status,
      user,
      signIn,
      signUp,
      signOut,
      resetPassword,
      sendVerification,
      refreshUser,
    ],
  );
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const auth = useContext(AuthContext);
  if (!auth) throw new Error("useAuth must be used inside AuthProvider");
  return auth;
}
