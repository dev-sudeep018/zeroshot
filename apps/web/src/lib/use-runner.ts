"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import {
  assertSeparateOrigin,
  BOOT_TIMEOUT_MS,
  EXECUTION_TIMEOUT_MS,
  PROTOCOL_VERSION,
  RunnerMessageSchema,
  type RunRequest,
  type RunResult,
} from "@zeroshot/runner-protocol";

export function useRunner(problemId: string, problemVersion: number) {
  const frame = useRef<HTMLIFrameElement>(null);
  const current = useRef<string | null>(null);
  const watchdog = useRef<ReturnType<typeof setTimeout> | null>(null);
  const [ready, setReady] = useState(false);
  const [phase, setPhase] = useState<"idle" | "loading" | "running">("idle");
  const [result, setResult] = useState<RunResult | null>(null);
  const [mode, setMode] = useState<RunRequest["mode"]>("sample");
  const [connectionError, setConnectionError] = useState("");
  const [frameKey, setFrameKey] = useState(0);
  const [allowedOrigin, setAllowedOrigin] = useState<string | null>(null);
  const origin =
    process.env.NEXT_PUBLIC_RUNNER_ORIGIN ?? "http://127.0.0.1:4174";

  useEffect(() => {
    let validatedOrigin: string;
    try {
      validatedOrigin = assertSeparateOrigin(location.origin, origin);
    } catch (e) {
      setAllowedOrigin(null);
      setReady(false);
      setConnectionError(String(e));
      return;
    }
    setAllowedOrigin(validatedOrigin);
    const handshake = setTimeout(
      () =>
        setConnectionError(
          "Python runner is unavailable. Start both local servers, then reconnect.",
        ),
      8000,
    );
    const onMessage = (event: MessageEvent) => {
      if (
        event.origin !== validatedOrigin ||
        event.source !== frame.current?.contentWindow
      )
        return;
      const parsed = RunnerMessageSchema.safeParse(event.data);
      if (!parsed.success) return;
      const message = parsed.data;
      if (message.kind === "ready") {
        clearTimeout(handshake);
        setReady(true);
        setConnectionError("");
        return;
      }
      if (message.requestId !== current.current) return;
      if (message.kind === "status") {
        setPhase(message.phase);
        return;
      }
      current.current = null;
      if (watchdog.current) clearTimeout(watchdog.current);
      setPhase("idle");
      setResult(message);
    };
    addEventListener("message", onMessage);
    frame.current?.contentWindow?.postMessage(
      { kind: "hello", protocol: PROTOCOL_VERSION },
      validatedOrigin,
    );
    return () => {
      removeEventListener("message", onMessage);
      clearTimeout(handshake);
      if (watchdog.current) clearTimeout(watchdog.current);
    };
  }, [origin, frameKey]);

  const run = useCallback(
    (sourceCode: string, selectedMode: RunRequest["mode"]) => {
      if (!ready || current.current) return;
      const requestId = crypto.randomUUID();
      current.current = requestId;
      setResult(null);
      setPhase("loading");
      setMode(selectedMode);
      frame.current?.contentWindow?.postMessage(
        {
          kind: "run",
          protocol: PROTOCOL_VERSION,
          requestId,
          problemId,
          problemVersion,
          sourceCode,
          mode: selectedMode,
        },
        origin,
      );
      watchdog.current = setTimeout(
        () => {
          if (current.current !== requestId) return;
          current.current = null;
          setPhase("idle");
          setReady(false);
          setFrameKey((k) => k + 1);
          setResult({
            kind: "result",
            protocol: PROTOCOL_VERSION,
            requestId,
            status: "error",
            tests: [],
            output: "",
            error:
              "The runner did not respond. It has been restarted; try again.",
            durationMs: 0,
          });
        },
        BOOT_TIMEOUT_MS + EXECUTION_TIMEOUT_MS + 3000,
      );
    },
    [origin, ready, problemId, problemVersion],
  );
  const cancel = useCallback(() => {
    if (current.current)
      frame.current?.contentWindow?.postMessage(
        {
          kind: "cancel",
          protocol: PROTOCOL_VERSION,
          requestId: current.current,
        },
        origin,
      );
  }, [origin]);
  function reconnect() {
    setConnectionError("");
    setReady(false);
    setFrameKey((k) => k + 1);
  }
  function hello() {
    frame.current?.contentWindow?.postMessage(
      { kind: "hello", protocol: PROTOCOL_VERSION },
      origin,
    );
  }
  return {
    frame,
    frameKey,
    origin: allowedOrigin,
    ready,
    phase,
    result,
    mode,
    connectionError,
    run,
    cancel,
    reconnect,
    hello,
  };
}
