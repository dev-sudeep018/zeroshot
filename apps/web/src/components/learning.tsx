"use client";
import Link from "next/link";
import { useState, type ChangeEvent } from "react";
import {
  ArrowRight,
  CheckCircle2,
  Circle,
  Download,
  Search,
  Upload,
} from "lucide-react";
import {
  beginnerTracks,
  catalog,
  domains,
  itemById,
  itemHref,
  paths,
} from "@/lib/curriculum";
import {
  BackupSchema,
  completed,
  exportBackup,
  importBackup,
  type Backup,
} from "@/lib/progress";
import { useProgress } from "@/lib/use-progress";
import { Experiment } from "./experiment";
import { MomentumPanel } from "./momentum";

export function PathList({ slug }: { slug?: string }) {
  const state = useProgress();
  const selected = slug ? paths.filter((path) => path.slug === slug) : paths;
  return (
    <>
      {selected.map((path) => {
        const done = path.items.filter((id) => completed(state, id)).length;
        const next = path.items.find((id) => !completed(state, id));
        return (
          <section
            className="learning-path"
            key={path.slug}
            data-path={path.slug}
          >
            <div className="section-heading">
              <div>
                <h2>{path.title}</h2>
                <p>{path.description}</p>
              </div>
              <span className="muted">
                {done}/{path.items.length} explored & checked
              </span>
            </div>
            <p className="path-outcome">You will be able to: {path.outcome}</p>
            {!slug ? (
              <Link className="primary" href={`/paths/${path.slug}/`}>
                {done ? "Continue this path" : "View this path"}
                <ArrowRight size={16} />
              </Link>
            ) : (
              <>
                <ol className="path-list">
                  {path.items.map((id, index) => {
                    const item = itemById(id)!;
                    const missing = item.prerequisites.filter(
                      (id) => !completed(state, id),
                    );
                    return (
                      <li key={id} className="available">
                        {completed(state, id) ? (
                          <CheckCircle2
                            className="step-icon success-text"
                            size={18}
                          />
                        ) : (
                          <Circle className="step-icon" size={18} />
                        )}
                        <div>
                          <span className="muted small">
                            Step {index + 1} · {item.estimated_minutes} min
                          </span>
                          <h3>
                            <Link href={itemHref(id)}>{item.title}</Link>
                          </h3>
                          <p>{item.summary}</p>
                          {missing.length > 0 && (
                            <p className="small">
                              Helpful first:{" "}
                              {missing.map((id, i) => (
                                <span key={id}>
                                  {i > 0 && ", "}
                                  <Link
                                    className="text-link"
                                    href={itemHref(id)}
                                  >
                                    {itemById(id)?.title}
                                  </Link>
                                </span>
                              ))}
                            </p>
                          )}
                          <Link className="text-link" href={itemHref(id)}>
                            {id === next
                              ? "Continue here"
                              : completed(state, id)
                                ? "Revisit the idea"
                                : "Open lesson"}
                            <ArrowRight size={14} />
                          </Link>
                        </div>
                      </li>
                    );
                  })}
                </ol>
                <Link className="secondary" href="/projects/mini-retrieval/">
                  Connect these ideas in a project
                  <ArrowRight size={16} />
                </Link>
              </>
            )}
          </section>
        );
      })}
    </>
  );
}

export function BeginnerEntry() {
  const count = catalog.filter((item) => item.difficulty === "beginner").length;
  return (
    <section className="beginner-entry" aria-labelledby="beginner-entry-title">
      <div>
        <h2 id="beginner-entry-title">
          Build your foundations through useful problems.
        </h2>
        <p>
          Start with records, arrays, and small model operations. These lessons
          assume basic Python and explain the data and ML ideas as you go.
        </p>
      </div>
      <div className="beginner-actions">
        <Link className="primary" href="/paths/start-here/">
          Explore the beginner route <ArrowRight size={16} />
        </Link>
        <Link className="text-link" href="/beginner/">
          Browse {count} beginner lessons <ArrowRight size={16} />
        </Link>
      </div>
    </section>
  );
}

export function BeginnerGuide() {
  const state = useProgress();
  return (
    <>
      {beginnerTracks.map((track) => (
        <section className="learning-path" key={track.title}>
          <div className="section-heading">
            <div>
              <h2>{track.title}</h2>
              <p>{track.description}</p>
            </div>
            <span className="muted">
              {track.items.filter((id) => completed(state, id)).length}/
              {track.items.length} checked
            </span>
          </div>
          <ol className="path-list">
            {track.items.map((id) => {
              const item = itemById(id);
              if (!item) return null;
              return (
                <li key={id} className="available">
                  {completed(state, id) ? (
                    <CheckCircle2
                      className="step-icon success-text"
                      size={18}
                    />
                  ) : (
                    <Circle className="step-icon" size={18} />
                  )}
                  <div>
                    <span className="muted small">
                      {item.estimated_minutes} min · {item.difficulty}
                    </span>
                    <h3>
                      <Link href={itemHref(id)}>{item.title}</Link>
                    </h3>
                    <p>{item.summary}</p>
                    <Link className="text-link" href={itemHref(id)}>
                      {completed(state, id)
                        ? "Revisit the idea"
                        : "Open lesson"}
                      <ArrowRight size={14} />
                    </Link>
                  </div>
                </li>
              );
            })}
          </ol>
        </section>
      ))}
      <Link className="primary" href="/beginner/">
        Explore all beginner lessons <ArrowRight size={16} />
      </Link>
    </>
  );
}

export function LessonCatalog({
  initialLevel = "all",
}: {
  initialLevel?: string;
}) {
  const state = useProgress();
  const [query, setQuery] = useState("");
  const [domain, setDomain] = useState("all");
  const [level, setLevel] = useState(initialLevel);
  const [status, setStatus] = useState("all");
  const [page, setPage] = useState(1);
  const filtered = catalog.filter(
    (item) =>
      (domain === "all" || item.domain === domain) &&
      (level === "all" || item.difficulty === level) &&
      (status === "all" ||
        (status === "completed") === completed(state, item.id)) &&
      `${item.title} ${item.summary} ${item.skills.join(" ")}`
        .toLowerCase()
        .includes(query.toLowerCase()),
  );
  const reset =
    (setter: (v: string) => void) =>
    (e: ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
      setter(e.target.value);
      setPage(1);
    };
  return (
    <>
      <div className="catalog-controls">
        <label className="search-field">
          <Search size={17} />
          <input
            aria-label="Search lessons"
            placeholder="Search a concept, skill, or question"
            value={query}
            onChange={reset(setQuery)}
          />
        </label>
        <label>
          Topic
          <select value={domain} onChange={reset(setDomain)}>
            <option value="all">Every topic</option>
            {Object.entries(domains).map(([key, title]) => (
              <option value={key} key={key}>
                {title}
              </option>
            ))}
          </select>
        </label>
        <label>
          Depth
          <select value={level} onChange={reset(setLevel)}>
            <option value="all">Every level</option>
            {["beginner", "intermediate", "advanced"].map((value) => (
              <option key={value}>{value}</option>
            ))}
          </select>
        </label>
        <label>
          Progress
          <select value={status} onChange={reset(setStatus)}>
            <option value="all">All lessons</option>
            <option value="new">Still exploring</option>
            <option value="completed">Checked</option>
          </select>
        </label>
      </div>
      <p className="muted small" role="status">
        {filtered.length} of {catalog.length} published lessons
      </p>
      <div className="lesson-list">
        {filtered.slice((page - 1) * 24, page * 24).map((item) => (
          <Link
            className="lesson-row"
            key={item.id}
            href={itemHref(item.id)}
            data-domain={item.domain}
          >
            <div>
              <span className="lesson-row-meta">
                <span className={`topic-label topic-${item.domain}`}>
                  {domains[item.domain]}
                </span>
                <span>{item.estimated_minutes} min</span>
              </span>
              <h2>{item.title}</h2>
              <p>{item.summary}</p>
              <span className="small muted">{item.skills.join(" · ")}</span>
            </div>
            <span
              className={`lesson-state${completed(state, item.id) ? " success-text" : ""}`}
            >
              {completed(state, item.id) ? (
                <CheckCircle2 size={18} />
              ) : (
                <ArrowRight size={18} />
              )}
              <span>
                {completed(state, item.id) ? "Checked" : item.difficulty}
              </span>
            </span>
          </Link>
        ))}
      </div>
      {filtered.length === 0 && (
        <div className="empty-state">
          <h2>No matching lessons yet.</h2>
          <p>Try a broader concept or reset the filters.</p>
          <button
            className="secondary"
            onClick={() => {
              setQuery("");
              setDomain("all");
              setLevel("all");
              setStatus("all");
            }}
          >
            Reset filters
          </button>
        </div>
      )}
      {filtered.length > 24 && (
        <div className="pagination">
          <button
            className="secondary"
            disabled={page === 1}
            onClick={() => setPage(page - 1)}
          >
            Previous
          </button>
          <span>
            Page {page} of {Math.ceil(filtered.length / 24)}
          </span>
          <button
            className="secondary"
            disabled={page * 24 >= filtered.length}
            onClick={() => setPage(page + 1)}
          >
            Next
          </button>
        </div>
      )}
    </>
  );
}

export function OpenLab() {
  const [id, setId] = useState("m02");
  return (
    <div className="open-lab">
      <div
        className="lab-topics"
        role="group"
        aria-label="Choose an experiment"
      >
        {[
          ["m02", "Probability & temperature"],
          ["m01", "Vector direction"],
          ["d01", "Gradient checks"],
          ["e01", "Chunk boundaries"],
        ].map(([value, title]) => (
          <button
            className={id === value ? "selected" : ""}
            aria-pressed={id === value}
            key={value}
            onClick={() => setId(value)}
          >
            {title}
          </button>
        ))}
      </div>
      <Experiment key={id} itemId={id} />
      <div className="lab-next">
        <h2>Take the idea into code</h2>
        <p>{itemById(id)?.summary}</p>
        <Link className="primary" href={itemHref(id)}>
          Open {itemById(id)?.title}
          <ArrowRight size={16} />
        </Link>
        <Link className="text-link" href="/problems/">
          Browse all {catalog.length} lessons
        </Link>
      </div>
    </div>
  );
}

export function downloadJson(filename: string, value: unknown) {
  const url = URL.createObjectURL(
    new Blob([JSON.stringify(value, null, 2)], { type: "application/json" }),
  );
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
export function ProgressView() {
  const state = useProgress();
  const [notice, setNotice] = useState("");
  const [noticeTone, setNoticeTone] = useState("info");
  const [pending, setPending] = useState<Backup | null>(null);
  const count = catalog.filter((item) => completed(state, item.id)).length;
  async function readImport(event: ChangeEvent<HTMLInputElement>) {
    setPending(null);
    const file = event.target.files?.[0];
    event.target.value = "";
    if (!file) return;
    try {
      if (file.size > 8_000_000)
        throw new Error("Backup exceeds the 8 MB import limit.");
      const parsed = BackupSchema.parse(JSON.parse(await file.text()));
      setPending(parsed);
      setNotice("");
    } catch {
      setNoticeTone("failure");
      setNotice(
        "That file is not a supported ZeroShot backup, or exceeds 8 MB. Choose an exported JSON backup.",
      );
    }
  }
  return (
    <>
      <h1>See how far you’ve come.</h1>
      <p className="page-lead">
        {count} of {catalog.length} lessons checked. Revisit an idea whenever
        you need it; progress is a record of your work, not a ranking.
      </p>
      <div id="momentum">
        <MomentumPanel />
      </div>
      <PathList />
      <section
        className="project-progress"
        aria-labelledby="project-progress-title"
      >
        <h2 id="project-progress-title">Your project work</h2>
        <p>
          {completed(state, "p01")
            ? "Retrieval pipeline checked. Return to the workbench to compare rankings and record what you learned."
            : "Connect the retrieval lessons in a Python pipeline, then investigate the results in the project workbench."}
        </p>
        <Link className="text-link" href="/projects/mini-retrieval/">
          Return to the retrieval project <ArrowRight size={16} />
        </Link>
      </section>
      <section className="backup-section">
        <h2>Keep a copy of your work</h2>
        <p>
          Export lesson progress, practice rewards, preferences, and code drafts
          to a file you control. Import merges progress and fills missing
          drafts; existing code on this device stays in place. Existing
          preferences are preserved; a new device restores your saved choices.
          Older Project Mastery backups still work. Project notes and reports
          have their own export in the project.
        </p>
        <div className="button-row">
          <button
            className="secondary"
            onClick={() => {
              try {
                downloadJson("zeroshot-backup.json", exportBackup());
                setNoticeTone("success");
                setNotice(
                  "Backup prepared with your lesson progress and code drafts.",
                );
              } catch {
                setNoticeTone("failure");
                setNotice(
                  "Could not read storage. Copy important code from the editor.",
                );
              }
            }}
          >
            <Download size={16} />
            Export backup
          </button>
          <label className="secondary file-button">
            <Upload size={16} />
            Choose backup
            <input
              type="file"
              accept=".json,application/json"
              onChange={readImport}
            />
          </label>
        </div>
        {pending && (
          <div className="inline-confirm">
            <p>
              Merge {Object.keys(pending.progress).length} progress records and
              up to {Object.keys(pending.drafts).length} missing drafts? Only
              matching published lesson versions are imported.
            </p>
            <button
              onClick={() => {
                try {
                  importBackup(pending);
                  setPending(null);
                  setNoticeTone("success");
                  setNotice("Backup merged. Existing drafts were preserved.");
                } catch {
                  setNoticeTone("warning");
                  setNotice(
                    "Storage is full or unavailable. Some records may have been imported; keep your backup.",
                  );
                }
              }}
            >
              Merge backup
            </button>
            <button onClick={() => setPending(null)}>Cancel import</button>
          </div>
        )}
        <p role="status" className={`${noticeTone}-text`}>
          {notice}
        </p>
        <p className="muted small">
          No account or cloud sync is active. Clearing browser storage removes
          local work; exporting a backup lets you move it to another device.
        </p>
      </section>
    </>
  );
}
