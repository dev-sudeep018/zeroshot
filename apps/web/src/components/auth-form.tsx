"use client";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useRef, useState, type FormEvent } from "react";
import {
  ArrowLeft,
  ArrowRight,
  CheckCircle2,
  Eye,
  EyeOff,
  Mail,
  ShieldCheck,
} from "lucide-react";
import { authErrorMessage, safeAuthRedirect } from "@/lib/auth";
import { useAuth } from "./auth-provider";

type Mode = "signin" | "signup" | "reset";
type Notice = { text: string; error?: boolean } | null;

function AuthNotice({ notice }: { notice: Notice }) {
  const ref = useRef<HTMLParagraphElement>(null);
  useEffect(() => {
    if (notice?.error) ref.current?.focus();
  }, [notice]);
  if (!notice) return null;
  return (
    <p
      ref={ref}
      tabIndex={-1}
      className={`auth-notice ${notice.error ? "is-error" : "is-success"}`}
      role={notice.error ? "alert" : "status"}
    >
      {notice.text}
    </p>
  );
}

export function AuthForm() {
  const auth = useAuth();
  const router = useRouter();
  const [mode, setMode] = useState<Mode>("signin");
  const [next, setNext] = useState("/learn/");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [busy, setBusy] = useState(false);
  const [notice, setNotice] = useState<Notice>(null);
  useEffect(() => {
    const query = new URLSearchParams(window.location.search);
    setNext(safeAuthRedirect(query.get("next")));
    const initialMode = query.get("mode");
    if (initialMode === "signup" || initialMode === "reset")
      setMode(initialMode);
  }, []);

  function changeMode(value: Mode) {
    setMode(value);
    setNotice(null);
    setPassword("");
    setShowPassword(false);
  }
  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (busy || auth.status !== "ready") return;
    setBusy(true);
    setNotice(null);
    try {
      if (mode === "reset") {
        await auth.resetPassword(email);
        setNotice({
          text: "If an account uses that email, a password reset link has been requested. Check your inbox and spam folder.",
        });
      } else if (mode === "signup") {
        const result = await auth.signUp(email, password);
        setPassword("");
        setNotice(
          result.verificationSent
            ? {
                text: "Your account is created. A verification email has been requested; open its link to verify your address.",
              }
            : {
                text: "Your account is created, but we couldn't request the verification email. Open your account to try again.",
                error: true,
              },
        );
      } else {
        await auth.signIn(email, password);
        setPassword("");
        router.replace(next);
      }
    } catch (error) {
      setNotice({ text: authErrorMessage(error, mode), error: true });
    } finally {
      setBusy(false);
    }
  }

  if (auth.status === "loading")
    return (
      <div className="auth-loading" role="status">
        <h1>Opening your account</h1>
        <p>Checking your saved session…</p>
      </div>
    );
  if (auth.status === "unavailable" || auth.status === "error")
    return (
      <div className="auth-unavailable">
        <h1>Keep learning as a guest</h1>
        <p>
          Account access{" "}
          {auth.status === "unavailable"
            ? "isn't enabled on this version yet"
            : "couldn't be loaded right now"}
          . Lessons, projects, and your saved work are still available.
        </p>
        <Link className="primary" href={next}>
          Open learning portal <ArrowRight size={17} />
        </Link>
        {auth.status === "error" && (
          <button
            className="secondary"
            onClick={() => window.location.reload()}
          >
            Try account access again
          </button>
        )}
      </div>
    );
  if (auth.user)
    return (
      <div className="auth-signed-in">
        <CheckCircle2 size={30} className="success-text" aria-hidden="true" />
        <h1>You’re signed in</h1>
        <p className="auth-email">{auth.user.email}</p>
        <AuthNotice notice={notice} />
        <p>
          {auth.user.emailVerified
            ? "Your email address is verified."
            : "Verify your email using the link in your inbox. You can continue learning while you do."}
        </p>
        <div className="auth-actions">
          <Link className="primary" href={next}>
            Continue learning <ArrowRight size={17} />
          </Link>
          <Link className="text-link" href="/account/">
            Manage your account
          </Link>
        </div>
      </div>
    );

  return (
    <>
      <div className="auth-title">
        <h1>
          {mode === "reset"
            ? "Reset your password"
            : mode === "signup"
              ? "Create your account"
              : "Welcome back"}
        </h1>
        <p>
          {mode === "reset"
            ? "Enter your email and we’ll request a reset link."
            : "A free ZeroShot account. Learning stays open to everyone."}
        </p>
      </div>
      {mode !== "reset" && (
        <div className="auth-mode" aria-label="Account action">
          <button
            type="button"
            aria-pressed={mode === "signin"}
            onClick={() => changeMode("signin")}
            disabled={busy}
          >
            Sign in
          </button>
          <button
            type="button"
            aria-pressed={mode === "signup"}
            onClick={() => changeMode("signup")}
            disabled={busy}
          >
            Create account
          </button>
        </div>
      )}
      <AuthNotice notice={notice} />
      <form className="auth-form" onSubmit={submit} aria-busy={busy}>
        <label htmlFor="account-email">Email address</label>
        <input
          id="account-email"
          type="email"
          autoComplete="email"
          autoCapitalize="none"
          spellCheck={false}
          required
          maxLength={254}
          value={email}
          onChange={(event) => setEmail(event.target.value)}
          disabled={busy}
        />
        {mode !== "reset" && (
          <>
            <label htmlFor="account-password">Password</label>
            <div className="auth-password">
              <input
                id="account-password"
                type={showPassword ? "text" : "password"}
                autoComplete={
                  mode === "signup" ? "new-password" : "current-password"
                }
                required
                minLength={mode === "signup" ? 8 : undefined}
                maxLength={4096}
                aria-describedby={
                  mode === "signup" ? "password-guidance" : undefined
                }
                value={password}
                onChange={(event) => setPassword(event.target.value)}
                disabled={busy}
              />
              <button
                type="button"
                aria-label={showPassword ? "Hide password" : "Show password"}
                aria-pressed={showPassword}
                onClick={() => setShowPassword(!showPassword)}
                disabled={busy}
              >
                {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
              </button>
            </div>
            {mode === "signup" && (
              <p id="password-guidance" className="auth-field-help">
                Use at least 8 characters. A longer, unique password is best.
              </p>
            )}
          </>
        )}
        {mode === "signin" && (
          <button
            className="auth-reset-link"
            type="button"
            onClick={() => changeMode("reset")}
            disabled={busy}
          >
            Forgot your password?
          </button>
        )}
        <button className="primary auth-submit" type="submit" disabled={busy}>
          {busy
            ? mode === "reset"
              ? "Requesting reset…"
              : mode === "signup"
                ? "Creating account…"
                : "Signing in…"
            : mode === "reset"
              ? "Send reset link"
              : mode === "signup"
                ? "Create account"
                : "Sign in"}
          <ArrowRight size={17} />
        </button>
      </form>
      {mode === "reset" && (
        <button
          className="text-link auth-back"
          onClick={() => changeMode("signin")}
          disabled={busy}
        >
          <ArrowLeft size={15} /> Back to sign in
        </button>
      )}
      <div className="auth-local-note">
        <ShieldCheck size={18} aria-hidden="true" />
        <p>
          Your code and progress stay in this browser. Accounts don’t sync
          learning data yet. You can export a backup from Your progress.
        </p>
      </div>
      <Link className="auth-guest" href={next}>
        Continue as a guest <ArrowRight size={15} />
      </Link>
    </>
  );
}

export function AccountDetails() {
  const auth = useAuth();
  const [busy, setBusy] = useState(false);
  const [notice, setNotice] = useState<Notice>(null);
  async function act(action: "verify" | "refresh" | "reset" | "signout") {
    if (busy) return;
    setBusy(true);
    setNotice(null);
    try {
      if (action === "verify") {
        await auth.sendVerification();
        setNotice({
          text: "A verification email has been requested. Check your inbox and spam folder.",
        });
      } else if (action === "refresh") {
        const verified = await auth.refreshUser();
        setNotice({
          text: verified
            ? "Your email is verified."
            : "Your email hasn't been verified yet. Open the link in your verification email, then check again.",
        });
      } else if (action === "reset" && auth.user?.email) {
        await auth.resetPassword(auth.user.email);
        setNotice({
          text: "A password reset link has been requested. Check your inbox and spam folder.",
        });
      } else if (action === "signout") {
        await auth.signOut();
        setNotice({
          text: "You’re signed out. Your code and progress remain saved in this browser.",
        });
      }
    } catch (error) {
      setNotice({ text: authErrorMessage(error, "account"), error: true });
    } finally {
      setBusy(false);
    }
  }
  return (
    <>
      <h1>Your account</h1>
      <p className="page-lead">Manage your sign-in and email verification.</p>
      <AuthNotice notice={notice} />
      {auth.status === "loading" ? (
        <p role="status">Checking your saved session…</p>
      ) : !auth.user ? (
        <section className="account-section">
          <h2>
            {auth.status === "ready"
              ? "You’re learning as a guest"
              : "Account access is unavailable"}
          </h2>
          <p>
            {auth.status === "ready"
              ? "You can sign in or create an account whenever you’re ready. Every lesson remains available without one."
              : "You can continue with every lesson and project while account access is being restored."}
          </p>
          <div className="auth-actions">
            {auth.status === "ready" && (
              <Link className="primary" href="/login/?next=/account/">
                Sign in or create an account <ArrowRight size={17} />
              </Link>
            )}
            <Link className="text-link" href="/learn/">
              Continue learning <ArrowRight size={15} />
            </Link>
          </div>
        </section>
      ) : (
        <>
          <section
            className="account-section"
            aria-labelledby="account-email-heading"
          >
            <h2 id="account-email-heading">Email and verification</h2>
            <p className="account-identity">
              <Mail size={18} aria-hidden="true" />
              <span>{auth.user.email}</span>
            </p>
            <p
              className={
                auth.user.emailVerified ? "success-text" : "warning-text"
              }
            >
              {auth.user.emailVerified
                ? "Email verified"
                : "Email verification needed"}
            </p>
            {!auth.user.emailVerified && (
              <>
                <p>
                  Open the verification link in your inbox, then check your
                  status here.
                </p>
                <div className="auth-actions">
                  <button
                    className="secondary"
                    disabled={busy}
                    onClick={() => void act("verify")}
                  >
                    Resend verification email
                  </button>
                  <button
                    className="text-link"
                    disabled={busy}
                    onClick={() => void act("refresh")}
                  >
                    I’ve verified my email
                  </button>
                </div>
              </>
            )}
          </section>
          <section
            className="account-section"
            aria-labelledby="account-security-heading"
          >
            <h2 id="account-security-heading">Sign-in security</h2>
            <p>Reset your password by email, or sign out on this browser.</p>
            <div className="auth-actions">
              <button
                className="secondary"
                disabled={busy}
                onClick={() => void act("reset")}
              >
                Request password reset
              </button>
              <button
                className="text-link"
                disabled={busy}
                onClick={() => void act("signout")}
              >
                Sign out
              </button>
            </div>
            {busy && <p role="status">Updating your account…</p>}
          </section>
        </>
      )}
      <section className="account-section account-local">
        <h2>Your work stays on this device</h2>
        <p>
          Signing in does not sync progress or code between devices yet. This
          browser’s saved work is shared by anyone who uses it, even after
          signing out. Export your learning backup before switching devices.
        </p>
        <Link className="text-link" href="/progress/">
          Manage progress and backups <ArrowRight size={15} />
        </Link>
      </section>
    </>
  );
}
