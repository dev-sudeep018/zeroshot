import { describe, expect, it } from "vitest";
import {
  authErrorMessage,
  localAuthEmulator,
  readAuthConfig,
  safeAuthRedirect,
} from "../../apps/web/src/lib/auth";

describe("account configuration", () => {
  const valid = {
    apiKey: `AIza${"a".repeat(35)}`,
    authDomain: "zeroshot-example.firebaseapp.com",
    projectId: "zeroshot-example",
    appId: "1:123456789:web:abcdef123456",
  };
  it("requires a complete public web configuration", () => {
    expect(readAuthConfig(valid)).toEqual(valid);
    for (const key of Object.keys(valid)) {
      expect(readAuthConfig({ ...valid, [key]: undefined })).toBeNull();
      expect(readAuthConfig({ ...valid, [key]: "" })).toBeNull();
    }
    expect(
      readAuthConfig({ ...valid, authDomain: "https://example.com/path" }),
    ).toBeNull();
    expect(readAuthConfig({ ...valid, apiKey: "your-api-key" })).toBeNull();
    expect(readAuthConfig({ ...valid, appId: "project-id" })).toBeNull();
  });
});

describe("account return destinations", () => {
  it("keeps real learning routes and their local filters or anchors", () => {
    for (const href of [
      "/learn/",
      "/problems/stable-softmax/",
      "/paths/start-here/",
      "/progress/#momentum",
      "/account/",
      "/beginner/?topic=foundations",
      "/projects/mini-retrieval/",
    ]) {
      expect(safeAuthRedirect(href)).toBe(href);
    }
  });
  it("rejects external origins, protocol-relative URLs, encoded separators and auth loops", () => {
    for (const href of [
      null,
      "",
      "https://evil.example/learn/",
      "//evil.example/learn/",
      "/\\evil.example/learn/",
      "javascript:alert(1)",
      " /learn/",
      "/learn/\n",
      "/%2f%2fevil.example/",
      "/problems/%5cevil/",
      "/login/?next=https://evil.example",
      "/api/delete",
      "/unknown/",
    ]) {
      expect(safeAuthRedirect(href)).toBe("/learn/");
    }
  });
});

describe("local authentication emulator boundary", () => {
  it("only accepts explicit local emulator URLs on a local application", () => {
    const local = (value: string | undefined, hostname = "localhost") =>
      localAuthEmulator(value, hostname, "development", "demo-zeroshot");
    expect(local("http://127.0.0.1:9099")).toBe("http://127.0.0.1:9099");
    for (const origin of [
      "zeroshot.pages.dev",
      "localhost.evil.example",
      "127.0.0.1.evil.example",
    ])
      expect(local("http://127.0.0.1:9099", origin)).toBeNull();
    for (const value of [
      undefined,
      "https://127.0.0.1:9099",
      "http://evil.example:9099",
      "http://127.0.0.1",
      "http://user:pass@127.0.0.1:9099",
      "http://127.0.0.1:9099/path",
      "http://127.0.0.1:9099/?redirect=1",
    ])
      expect(local(value)).toBeNull();
    for (const environment of ["production", "test", undefined])
      expect(
        localAuthEmulator(
          "http://127.0.0.1:9099",
          "localhost",
          environment,
          "demo-zeroshot",
        ),
      ).toBeNull();
    expect(
      localAuthEmulator(
        "http://127.0.0.1:9099",
        "localhost",
        "development",
        "zeroshot-production",
      ),
    ).toBeNull();
  });
});

describe("account error messages", () => {
  it("does not expose account existence during sign-in", () => {
    const generic = authErrorMessage(
      { code: "auth/invalid-credential" },
      "signin",
    );
    for (const code of [
      "auth/user-not-found",
      "auth/wrong-password",
      "auth/user-disabled",
      "auth/email-already-in-use",
    ]) {
      expect(authErrorMessage({ code }, "signin")).toBe(generic);
    }
    expect(
      authErrorMessage({ code: "auth/email-already-in-use" }, "signup"),
    ).not.toMatch(/already|exists|registered/i);
  });
  it("shows recoverable connection and configuration failures without raw provider data", () => {
    expect(
      authErrorMessage({ code: "auth/network-request-failed" }, "signin"),
    ).toMatch(/internet/);
    expect(
      authErrorMessage({ code: "auth/too-many-requests" }, "signup"),
    ).toMatch(/Wait/);
    expect(
      authErrorMessage({ code: "auth/operation-not-allowed" }, "signin"),
    ).toMatch(/guest/);
    expect(
      authErrorMessage(new Error("secret-provider-diagnostics"), "account"),
    ).not.toContain("secret-provider-diagnostics");
  });
});
