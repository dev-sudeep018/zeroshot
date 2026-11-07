export type AuthEnvironment = {
  apiKey?: string;
  authDomain?: string;
  projectId?: string;
  appId?: string;
};

export function readAuthConfig(environment: AuthEnvironment) {
  const apiKey = environment.apiKey?.trim();
  const authDomain = environment.authDomain?.trim();
  const projectId = environment.projectId?.trim();
  const appId = environment.appId?.trim();
  if (
    !apiKey ||
    !authDomain ||
    !projectId ||
    !appId ||
    !/^[a-z0-9][a-z0-9.-]*[a-z0-9]$/i.test(authDomain) ||
    !/^[a-z][a-z0-9-]{4,29}$/.test(projectId) ||
    !/^1:\d+:web:[a-f0-9]+$/i.test(appId) ||
    !/^AIza[\w-]{30,}$/.test(apiKey)
  )
    return null;
  return { apiKey, authDomain, projectId, appId };
}

/** Only application destinations are accepted, never a caller-provided origin. */
export function safeAuthRedirect(candidate: string | null | undefined) {
  if (
    !candidate ||
    !candidate.startsWith("/") ||
    candidate.startsWith("//") ||
    candidate.includes("\\") ||
    [...candidate].some((character) => character.charCodeAt(0) <= 32)
  )
    return "/learn/";
  try {
    const url = new URL(candidate, "https://zeroshot.invalid");
    if (
      url.origin !== "https://zeroshot.invalid" ||
      /%|\.{2}/.test(url.pathname)
    )
      return "/learn/";
    const allowed =
      /^\/(?:learn|progress|account|beginner|explore)\/?$/.test(url.pathname) ||
      /^\/(?:problems|paths)(?:\/[a-z0-9-]+)?\/?$/.test(url.pathname) ||
      url.pathname === "/projects/mini-retrieval/";
    return allowed ? `${url.pathname}${url.search}${url.hash}` : "/learn/";
  } catch {
    return "/learn/";
  }
}

/** Emulated accounts must never be accepted on a public deployment. */
export function localAuthEmulator(
  value: string | undefined,
  hostname: string,
  environment: string | undefined,
  projectId: string,
) {
  if (
    environment !== "development" ||
    !projectId.startsWith("demo-") ||
    !value ||
    !["localhost", "127.0.0.1"].includes(hostname)
  )
    return null;
  try {
    const url = new URL(value);
    if (
      url.protocol !== "http:" ||
      !["localhost", "127.0.0.1"].includes(url.hostname) ||
      !url.port ||
      url.username ||
      url.password ||
      url.pathname !== "/" ||
      url.search ||
      url.hash
    )
      return null;
    return url.origin;
  } catch {
    return null;
  }
}

export function authErrorCode(error: unknown) {
  return error &&
    typeof error === "object" &&
    "code" in error &&
    typeof error.code === "string"
    ? error.code
    : "unknown";
}

export function authErrorMessage(
  error: unknown,
  action: "signin" | "signup" | "reset" | "account",
) {
  const code = authErrorCode(error);
  if (code === "auth/network-request-failed")
    return "We couldn't connect. Check your internet connection and try again.";
  if (code === "auth/too-many-requests" || code === "auth/quota-exceeded")
    return "Too many attempts right now. Wait a little before trying again.";
  if (code === "auth/invalid-email") return "Enter a valid email address.";
  if (
    code === "auth/weak-password" ||
    code === "auth/password-does-not-meet-requirements"
  )
    return "Choose a stronger password. Use at least 8 characters, with a mix of letters, numbers, and symbols.";
  if (
    code === "auth/requires-recent-login" ||
    code === "auth/user-token-expired" ||
    code === "auth/invalid-user-token"
  )
    return "Your session needs to be refreshed. Sign out and sign in again.";
  if (
    [
      "auth/operation-not-allowed",
      "auth/unauthorized-domain",
      "auth/invalid-api-key",
      "auth/app-not-authorized",
      "auth/configuration-not-found",
    ].includes(code)
  )
    return "Account access is temporarily unavailable. You can continue learning as a guest.";
  if (action === "signin")
    return "We couldn't sign you in with those details. Check your email and password, or reset your password.";
  if (action === "signup")
    return "We couldn't create that account. Try signing in or resetting your password.";
  if (action === "reset")
    return "We couldn't request a reset right now. Please try again shortly.";
  return "We couldn't complete that change. Please try again.";
}
