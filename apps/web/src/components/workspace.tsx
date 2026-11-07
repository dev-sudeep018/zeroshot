"use client";
import dynamic from "next/dynamic";
import Link from "next/link";
import { useCallback, useEffect, useRef, useState } from "react";
import type { OnMount } from "@monaco-editor/react";
import {
  ArrowLeft,
  ArrowRight,
  Check,
  CheckCircle2,
  ChevronRight,
  Circle,
  Clock3,
  Code2,
  Copy,
  Expand,
  Lightbulb,
  LoaderCircle,
  Play,
  RotateCcw,
  ShieldCheck,
  Square,
  Terminal,
  XCircle,
} from "lucide-react";
import { MAX_SOURCE_LENGTH } from "@zeroshot/runner-protocol";
import type { LearningItem } from "@zeroshot/problem-schema";
import { domains, itemById, itemHref, pathFor } from "@/lib/curriculum";
import {
  draftKey,
  completionKey,
  recordVisit,
  completed as isCompleted,
  readProgress,
} from "@/lib/progress";
import { Experiment } from "./experiment";
import { readDraft } from "@/lib/draft";
import { useRunner } from "@/lib/use-runner";
import { Shell } from "./shell";
import { useMomentum } from "@/lib/use-momentum";

const Editor = dynamic(() => import("./python-editor"), {
  ssr: false,
  loading: () => <div className="editor-loading">Loading code editor…</div>,
});
const resourceTabs = ["description", "hints", "solution"] as const;
export function Workspace({ data }: { data: LearningItem }) {
  const { problem, lesson } = data;
  const samples = lesson.examples;
  const DRAFT_KEY = draftKey(problem.id, problem.version);
  const PROGRESS_KEY = completionKey(problem.id, problem.version);
  const learningPath = pathFor(problem.id);
  const nextId =
    learningPath?.items[(learningPath.items.indexOf(problem.id) ?? -1) + 1];
  const [tab, setTab] = useState<"description" | "hints" | "solution">(
    "description",
  );
  const [code, setCode] = useState(data.starter);
  const [hydrated, setHydrated] = useState(false);
  const [saveState, setSaveState] = useState("Saved on this device");
  const [complete, setComplete] = useState(false);
  const [earnedXp, setEarnedXp] = useState(0);
  const { momentum } = useMomentum();
  const [pendingReplacement, setPendingReplacement] = useState<
    "starter" | "reference" | null
  >(null);
  const [copied, setCopied] = useState(false);
  const [focus, setFocus] = useState(false);
  const [split, setSplit] = useState(44);
  const [mobileEditor, setMobileEditor] = useState(false);
  const runner = useRunner(problem.id, problem.version);
  const splitRef = useRef<HTMLDivElement>(null);
  const runRef = useRef<() => void>(() => {});
  const busy = runner.phase !== "idle";
  const resultTone =
    runner.result?.status === "passed"
      ? "success"
      : runner.result?.status === "timeout"
        ? "warning"
        : runner.result?.status === "cancelled"
          ? "info"
          : "failure";
  const ResultIcon =
    runner.result?.status === "passed"
      ? CheckCircle2
      : runner.result?.status === "timeout"
        ? Clock3
        : runner.result?.status === "cancelled"
          ? Square
          : XCircle;

  useEffect(() => {
    try {
      setCode(readDraft(localStorage.getItem(DRAFT_KEY), data.starter));
      setComplete(isCompleted(readProgress(), problem.id));
      recordVisit(problem.id, problem.version);
    } catch {
      setSaveState("Storage unavailable. Copy your code before leaving.");
    }
    setHydrated(true);
  }, [DRAFT_KEY, PROGRESS_KEY, data.starter, problem.id, problem.version]);
  useEffect(() => {
    const refresh = () => setComplete(isCompleted(readProgress(), problem.id));
    addEventListener("storage", refresh);
    return () => removeEventListener("storage", refresh);
  }, [problem.id]);
  useEffect(() => {
    if (!hydrated) return;
    if (code.length > MAX_SOURCE_LENGTH) {
      setSaveState("Draft too large to save. Copy your code before leaving.");
      return;
    }
    try {
      localStorage.setItem(DRAFT_KEY, JSON.stringify({ version: 1, code }));
      setSaveState("Saved on this device");
    } catch {
      setSaveState("Could not save. Copy your code before leaving.");
    }
  }, [code, hydrated, DRAFT_KEY]);
  useEffect(() => {
    if (runner.result && runner.mode === "all") {
      try {
        const firstPass = recordVisit(
          problem.id,
          problem.version,
          runner.result.status === "passed",
        );
        setEarnedXp(firstPass ? (problem.kind === "project" ? 30 : 10) : 0);
      } catch {
        setEarnedXp(0);
        setSaveState(
          "Checks finished, but progress could not be fully saved. Keep a backup or copy your code.",
        );
      }
    }
    if (runner.result?.status === "passed" && runner.mode === "all") {
      setComplete(true);
      try {
        localStorage.setItem(PROGRESS_KEY, "complete");
      } catch {
        /* Saving status is handled by the draft notice. */
      }
    }
  }, [
    runner.result,
    runner.mode,
    PROGRESS_KEY,
    problem.id,
    problem.version,
    problem.kind,
  ]);
  const checkSolution = useCallback(() => {
    if (!busy && code.length <= MAX_SOURCE_LENGTH) runner.run(code, "all");
  }, [busy, code, runner]);
  useEffect(() => {
    runRef.current = checkSolution;
  }, [checkSolution]);
  useEffect(() => {
    const handle = (event: KeyboardEvent) => {
      if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
        event.preventDefault();
        runRef.current();
      }
      if (event.key === "Escape") setFocus(false);
    };
    addEventListener("keydown", handle);
    return () => removeEventListener("keydown", handle);
  }, []);
  const mountEditor: OnMount = (editor, monaco) => {
    // The React wrapper creates the model before editor options are applied.
    editor.getModel()?.updateOptions({
      bracketColorizationOptions: {
        enabled: false,
        independentColorPoolPerBracketType: false,
      },
    });
    const palette = getComputedStyle(document.documentElement);
    const color = (name: string) =>
      palette.getPropertyValue(`--${name}`).trim();
    monaco.editor.defineTheme("mastery", {
      base: "vs-dark",
      inherit: false,
      rules: [
        { token: "", foreground: color("text").slice(1) },
        {
          token: "comment",
          foreground: color("subtle").slice(1),
          fontStyle: "italic",
        },
        {
          token: "keyword",
          foreground: color("syntax-keyword").slice(1),
          fontStyle: "bold",
        },
        { token: "string", foreground: color("syntax-string").slice(1) },
        { token: "number", foreground: color("syntax-number").slice(1) },
      ],
      colors: {
        "editor.background": color("surface"),
        "editor.foreground": color("text"),
        "editorLineNumber.foreground": color("subtle"),
        "editorLineNumber.activeForeground": color("text"),
        "editor.lineHighlightBackground": color("raised"),
        "editor.selectionBackground": color("selection"),
        "editorCursor.foreground": color("accent"),
        "editorIndentGuide.background1": color("border"),
        "editorBracketMatch.background": color("raised"),
        "editorBracketMatch.border": color("border-strong"),
        "editorBracketHighlight.foreground1": color("text"),
        "editorBracketHighlight.foreground2": color("text"),
        "editorBracketHighlight.foreground3": color("text"),
        "editorBracketHighlight.foreground4": color("text"),
        "editorBracketHighlight.foreground5": color("text"),
        "editorBracketHighlight.foreground6": color("text"),
        "editorBracketHighlight.unexpectedBracket.foreground": color("danger"),
        "editorError.foreground": color("danger"),
        "editorWarning.foreground": color("warning"),
        "editorInfo.foreground": color("info"),
        focusBorder: color("accent"),
        "editorWidget.background": color("raised"),
        "editorWidget.border": color("border-strong"),
        "input.background": color("surface"),
        "input.foreground": color("text"),
        "input.border": color("border-strong"),
        "editorSuggestWidget.background": color("raised"),
        "editorSuggestWidget.foreground": color("text"),
        "editorSuggestWidget.selectedBackground": color("selection"),
        "editorSuggestWidget.highlightForeground": color("accent"),
      },
    });
    monaco.editor.setTheme("mastery");
    editor.addAction({
      id: "mastery-check",
      label: "Check solution",
      keybindings: [monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter],
      run: () => runRef.current(),
    });
  };
  const passed = runner.result?.tests.filter((t) => t.passed).length ?? 0;
  function resize(clientX: number) {
    const box = splitRef.current?.getBoundingClientRect();
    if (box)
      setSplit(
        Math.min(62, Math.max(30, ((clientX - box.left) / box.width) * 100)),
      );
  }
  async function copyCode() {
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      setTimeout(() => setCopied(false), 1800);
    } catch {
      setSaveState("Copy unavailable. Select the code and press Ctrl+C.");
    }
  }

  return (
    <Shell workspace>
      <header className="topbar">
        <div className="breadcrumb">
          <Link href="/problems/">Explore lessons</Link>
          <ChevronRight size={14} />
          <span>{domains[problem.domain]}</span>
        </div>
        <span className="free-label">
          <ShieldCheck size={15} />
          Free & open source
        </span>
      </header>
      <div className="problem-header">
        <div>
          <Link className="back-link" href="/problems/">
            <ArrowLeft size={14} />
            All lessons
          </Link>
          <h1>{problem.title}</h1>
          <div className="problem-meta">
            <span className="difficulty">{problem.difficulty}</span>
            <span>
              <Clock3 size={14} />
              {problem.estimated_minutes} min
            </span>
            <span>NumPy</span>
            <span className={complete ? "complete-label" : ""}>
              {complete ? (
                <>
                  <CheckCircle2 size={14} />
                  Completed on this device
                </>
              ) : (
                `${problem.id.toUpperCase()} · ${domains[problem.domain]}`
              )}
            </span>
          </div>
        </div>
        <Link
          className="path-link"
          href={
            problem.kind === "project"
              ? "/projects/mini-retrieval/"
              : `/paths/${learningPath?.slug ?? ""}/`
          }
        >
          {problem.kind === "project"
            ? "Return to the project"
            : "Your learning path"}
          <ArrowRight size={16} />
        </Link>
      </div>
      <div className="mobile-switch" role="group" aria-label="Workspace view">
        <button
          className={!mobileEditor ? "selected" : ""}
          aria-pressed={!mobileEditor}
          onClick={() => setMobileEditor(false)}
        >
          Read exercise
        </button>
        <button
          className={mobileEditor ? "selected" : ""}
          aria-pressed={mobileEditor}
          onClick={() => setMobileEditor(true)}
        >
          Write Python
        </button>
      </div>
      <div
        ref={splitRef}
        className={`workbench ${focus ? "editor-focused" : ""} ${mobileEditor ? "mobile-code" : ""}`}
        style={{ "--split": `${split}%` } as React.CSSProperties}
      >
        <section className="problem-panel" aria-label="Problem information">
          <div className="tabbar" role="tablist" aria-label="Problem resources">
            {resourceTabs.map((t, index) => (
              <button
                key={t}
                id={`tab-${t}`}
                role="tab"
                aria-selected={tab === t}
                aria-controls={`panel-${t}`}
                tabIndex={tab === t ? 0 : -1}
                onKeyDown={(event) => {
                  const next =
                    event.key === "Home"
                      ? 0
                      : event.key === "End"
                        ? resourceTabs.length - 1
                        : event.key === "ArrowRight"
                          ? (index + 1) % resourceTabs.length
                          : event.key === "ArrowLeft"
                            ? (index + resourceTabs.length - 1) %
                              resourceTabs.length
                            : null;
                  if (next === null) return;
                  event.preventDefault();
                  setTab(resourceTabs[next]);
                  document.getElementById(`tab-${resourceTabs[next]}`)?.focus();
                }}
                onClick={() => setTab(t)}
              >
                {t === "hints" && <Lightbulb size={15} />}
                {
                  {
                    description: "Description",
                    hints: "Hints",
                    solution: "Solution",
                  }[t]
                }
              </button>
            ))}
          </div>
          <div
            className="problem-content"
            role="tabpanel"
            id={`panel-${tab}`}
            aria-labelledby={`tab-${tab}`}
          >
            {tab === "description" && (
              <>
                <h2>Understand the idea</h2>
                <p>{lesson.intro}</p>
                {lesson.formula && (
                  <div className="formula">{lesson.formula}</div>
                )}
                <Experiment itemId={problem.id} compact />
                <h3>Build it in Python</h3>
                <p>{lesson.task}</p>
                <pre className="signature">
                  <code>def {lesson.signature}:</code>
                </pre>
                <h3>See it in numbers</h3>
                {lesson.examples.map((example) => (
                  <div className="example-block" key={example.name}>
                    <strong>{example.name}</strong>
                    <div>
                      <span>Input</span>
                      <code>{example.input}</code>
                    </div>
                    <div>
                      <span>Output</span>
                      <code>{example.output}</code>
                    </div>
                  </div>
                ))}
                <h3>Requirements</h3>
                <ul className="requirements">
                  {lesson.requirements.map((text) => (
                    <li key={text}>{text}</li>
                  ))}
                </ul>
                <p className="muted small">
                  Absolute tolerance: {problem.evaluation.absolute_tolerance} ·
                  Relative tolerance: {problem.evaluation.relative_tolerance}
                </p>
                <div className="knowledge">
                  <h3>Connect the idea</h3>
                  <p>{problem.assumed_knowledge.join(" · ")}</p>
                  {problem.prerequisites.map((id) => (
                    <p key={id}>
                      <Link className="text-link" href={itemHref(id)}>
                        Revisit {itemById(id)?.title}
                      </Link>
                    </p>
                  ))}
                  {problem.domain === "engineering" && (
                    <p>
                      <Link
                        className="text-link"
                        href="/projects/mini-retrieval/"
                      >
                        Explore the retrieval project
                      </Link>
                    </p>
                  )}
                  {nextId && (
                    <p>
                      <Link className="text-link" href={itemHref(nextId)}>
                        Continue with {itemById(nextId)?.title}
                      </Link>
                    </p>
                  )}
                </div>
              </>
            )}
            {tab === "hints" && (
              <>
                <h2>A nudge, when you need it.</h2>
                <p>
                  Open one hint at a time. Try the next step in your code before
                  continuing.
                </p>
                {lesson.hints.map(({ title, body }, i) => (
                  <details className="hint" key={title}>
                    <summary>
                      Hint {i + 1}: {title}
                    </summary>
                    <p>{body}</p>
                  </details>
                ))}
              </>
            )}
            {tab === "solution" && (
              <>
                <h2>Understand the reference.</h2>
                <p>
                  Compare the steps with your approach, then change an input and
                  predict what will happen.
                </p>
                <pre className="reference-code">{data.solution}</pre>
                <button
                  className="secondary"
                  onClick={() => {
                    setPendingReplacement("reference");
                    setMobileEditor(true);
                  }}
                >
                  <Code2 size={15} />
                  Use reference in editor
                </button>
                <h3>Why this works</h3>
                {lesson.explanation.map((text) => (
                  <p key={text}>{text}</p>
                ))}
                <p className="muted small">
                  All evaluation tests are public. Completion is local practice
                  feedback.
                </p>
              </>
            )}
          </div>
        </section>
        <div
          className="resize-handle"
          role="separator"
          aria-label="Resize problem and code panels"
          aria-orientation="vertical"
          aria-valuenow={Math.round(split)}
          aria-valuemin={30}
          aria-valuemax={62}
          tabIndex={0}
          onKeyDown={(e) => {
            if (e.key === "ArrowLeft" || e.key === "ArrowRight") {
              e.preventDefault();
              setSplit((s) =>
                Math.min(
                  62,
                  Math.max(30, s + (e.key === "ArrowRight" ? 2 : -2)),
                ),
              );
            }
          }}
          onPointerDown={(e) => {
            e.currentTarget.setPointerCapture(e.pointerId);
          }}
          onPointerMove={(e) => {
            if (e.currentTarget.hasPointerCapture(e.pointerId))
              resize(e.clientX);
          }}
          onPointerUp={(e) =>
            e.currentTarget.releasePointerCapture(e.pointerId)
          }
        >
          <span />
        </div>
        <section className="coding-panel" aria-label="Python workspace">
          <div className="editor-toolbar">
            <span className="filename">
              <Code2 size={16} />
              solution.py
            </span>
            <div>
              <span className="runtime-label">Python · NumPy</span>
              <button
                className="icon-button"
                aria-label={copied ? "Code copied" : "Copy code"}
                title="Copy code"
                onClick={copyCode}
              >
                {copied ? <Check size={16} /> : <Copy size={16} />}
              </button>
              <button
                className="icon-button"
                aria-label="Reset starter code"
                title="Reset starter code"
                onClick={() => setPendingReplacement("starter")}
              >
                <RotateCcw size={16} />
              </button>
              <button
                className="icon-button focus-button"
                aria-label={focus ? "Exit focus mode" : "Focus on editor"}
                title="Focus on editor"
                onClick={() => setFocus((f) => !f)}
              >
                <Expand size={16} />
              </button>
            </div>
          </div>
          {pendingReplacement && (
            <div className="inline-confirm" role="status">
              <span>
                Replace your current code with{" "}
                {pendingReplacement === "reference"
                  ? "the reference solution"
                  : "the starter"}
                ?
              </span>
              <button
                onClick={() => {
                  setCode(
                    pendingReplacement === "reference"
                      ? data.solution
                      : data.starter,
                  );
                  setPendingReplacement(null);
                }}
              >
                Replace code
              </button>
              <button onClick={() => setPendingReplacement(null)}>
                Keep my code
              </button>
            </div>
          )}
          <div className="editor-container">
            {hydrated && (
              <Editor
                height="100%"
                language="python"
                path="solution.py"
                value={code}
                onChange={(value) => {
                  setCode(value ?? "");
                  setSaveState("Saving…");
                }}
                onMount={mountEditor}
                theme="vs-dark"
                options={{
                  minimap: { enabled: false },
                  bracketPairColorization: { enabled: false },
                  fontSize: 14,
                  lineHeight: 24,
                  fontFamily: 'Consolas, "Liberation Mono", monospace',
                  padding: { top: 20, bottom: 20 },
                  scrollBeyondLastLine: false,
                  automaticLayout: true,
                  tabSize: 4,
                  wordWrap: "on",
                  renderLineHighlight: "line",
                  lineNumbersMinChars: 3,
                  glyphMargin: false,
                  folding: false,
                  ariaLabel: "Python code editor",
                  accessibilitySupport: "on",
                }}
              />
            )}
          </div>
          <div className="editor-status">
            <span
              className={
                saveState === "Saved on this device" ? "" : "warning-text"
              }
            >
              {saveState}
            </span>
            <span>
              UTF-8<span className="status-divider">·</span>4 spaces
            </span>
          </div>
          <div className="run-toolbar">
            <span className="shortcut">
              <kbd>Ctrl</kbd> + <kbd>Enter</kbd> to check
            </span>
            <div>
              {busy ? (
                <button className="secondary" onClick={runner.cancel}>
                  <Square size={13} />
                  Stop run
                </button>
              ) : (
                <button
                  className="secondary"
                  disabled={!runner.ready || code.length > MAX_SOURCE_LENGTH}
                  onClick={() => runner.run(code, "sample")}
                >
                  <Play size={14} />
                  Run examples
                </button>
              )}
              <button
                className="primary"
                disabled={
                  !runner.ready || busy || code.length > MAX_SOURCE_LENGTH
                }
                onClick={checkSolution}
              >
                {busy ? (
                  <LoaderCircle className="spin" size={16} />
                ) : (
                  <Check size={17} />
                )}
                Check solution
              </button>
            </div>
          </div>
          {code.length > MAX_SOURCE_LENGTH && (
            <p className="error-notice" role="alert">
              Code exceeds 32,000 characters. Shorten it before running.
            </p>
          )}
          <div className="results-panel">
            <div className="results-heading">
              <span>
                <Terminal size={16} />
                Test results
              </span>
              <span
                className={
                  busy
                    ? "info-text"
                    : runner.result
                      ? `${resultTone}-text`
                      : "muted"
                }
                aria-live="polite"
              >
                {busy
                  ? runner.phase === "loading"
                    ? "Loading Python…"
                    : "Running tests…"
                  : runner.result
                    ? runner.result.status === "timeout"
                      ? "Timed out"
                      : runner.result.status === "cancelled"
                        ? "Stopped"
                        : runner.result.status === "error"
                          ? "Python error"
                          : `${passed}/${runner.result.tests.length} passed`
                    : "Ready for your first run"}
              </span>
            </div>
            <div
              className="results-body"
              aria-live="polite"
              aria-atomic="false"
            >
              {runner.connectionError ? (
                <div className="run-notice error">
                  <XCircle size={20} />
                  <div>
                    <strong>Runner unavailable</strong>
                    <p>{runner.connectionError}</p>
                    <button className="secondary" onClick={runner.reconnect}>
                      Reconnect
                    </button>
                  </div>
                </div>
              ) : busy ? (
                <div className="run-notice">
                  <LoaderCircle className="spin" size={22} />
                  <div>
                    <strong>
                      {runner.phase === "loading"
                        ? "Preparing Python and NumPy"
                        : "Checking your implementation"}
                    </strong>
                    <p>
                      {runner.phase === "loading"
                        ? "The first run takes a little longer. Your code stays on this device."
                        : "Each run uses a fresh Python environment."}
                    </p>
                  </div>
                </div>
              ) : runner.result ? (
                <>
                  <div className={`result-summary ${resultTone}`}>
                    <ResultIcon size={19} />
                    <div>
                      <strong>
                        {runner.result.status === "passed"
                          ? runner.mode === "all"
                            ? "All checks passed. Nicely done."
                            : "Examples passed. Try the full checks next."
                          : runner.result.status === "timeout"
                            ? "Time limit reached"
                            : runner.result.status === "cancelled"
                              ? "Run stopped"
                              : runner.result.status === "error"
                                ? "Python needs a fix"
                                : "Keep going. Here’s what to check."}
                      </strong>
                      <span>
                        {runner.result.durationMs} ms ·{" "}
                        {runner.mode === "all"
                          ? "Full public test suite"
                          : "Example tests"}
                      </span>
                    </div>
                  </div>
                  {earnedXp > 0 &&
                    momentum.enabled &&
                    runner.mode === "all" &&
                    runner.result.status === "passed" && (
                      <div className="completion-reward" role="status">
                        <CheckCircle2 size={19} aria-hidden="true" />
                        <div>
                          <strong>
                            +{earnedXp} XP · First full check complete
                          </strong>
                          <p>
                            Explain why your solution works, then try the next
                            idea.
                          </p>
                          <Link
                            className="text-link"
                            href="/progress/#momentum"
                          >
                            See your milestones <ArrowRight size={14} />
                          </Link>
                        </div>
                      </div>
                    )}
                  {runner.result.error && (
                    <pre className={`error-output ${resultTone}`}>
                      {runner.result.error}
                    </pre>
                  )}
                  {runner.result.tests.map((test) => (
                    <details
                      className={`test-row ${test.passed ? "passed" : "failed"}`}
                      key={test.name}
                    >
                      <summary>
                        {test.passed ? (
                          <CheckCircle2 size={15} />
                        ) : (
                          <XCircle size={15} />
                        )}
                        <span>{test.name}</span>
                        <span>{test.passed ? "Passed" : "Failed"}</span>
                        <ChevronRight size={13} />
                      </summary>
                      <p>{test.message}</p>
                    </details>
                  ))}
                  {runner.result.output && (
                    <>
                      <h3 className="output-label">Console output</h3>
                      <pre className="console-output">
                        {runner.result.output}
                      </pre>
                    </>
                  )}
                </>
              ) : (
                <div className="sample-tests">
                  {samples.map((sample, i) => (
                    <details className="test-row" key={sample.name}>
                      <summary>
                        <Circle size={14} />
                        <span>
                          Example {i + 1}: {sample.name}
                        </span>
                        <ChevronRight size={13} />
                      </summary>
                      <p>
                        Input: <code>{sample.input}</code>
                        <br />
                        Expected: <code>{sample.output}</code>
                      </p>
                    </details>
                  ))}
                  <p className="test-help">
                    Run examples to explore. Check solution to test all{" "}
                    {lesson.test_count}
                    cases.
                  </p>
                </div>
              )}
            </div>
          </div>
          <div className="privacy-note">
            <ShieldCheck size={13} />
            Runs on your device. Results are practice feedback.
          </div>
        </section>
      </div>
      {runner.origin && (
        <iframe
          ref={runner.frame}
          key={runner.frameKey}
          src={runner.origin}
          onLoad={runner.hello}
          title="Isolated Python execution"
          sandbox="allow-scripts allow-same-origin"
          referrerPolicy="no-referrer"
          className="runner-frame"
          aria-hidden="true"
          tabIndex={-1}
        />
      )}
    </Shell>
  );
}
