"use client";
import Link from "next/link";
import {
  ArrowRight,
  CheckCircle2,
  Clock3,
  FlaskConical,
  FolderCode,
  Network,
  Search,
  Sigma,
  Workflow,
} from "lucide-react";
import { catalog, domains, itemHref, paths } from "@/lib/curriculum";
import { completed } from "@/lib/progress";
import { selectNextLesson } from "@/lib/momentum";
import { useProgress } from "@/lib/use-progress";
import { useMomentum } from "@/lib/use-momentum";
import { MomentumPanel } from "./momentum";
const pathIcons = [Sigma, Network, Workflow];

export function LearningDashboard() {
  const state = useProgress();
  const { momentum, ready } = useMomentum();
  const recent = catalog
    .filter((item) => state[`${item.id}:v${item.version}`])
    .sort(
      (a, b) =>
        (state[`${b.id}:v${b.version}`]?.updatedAt ?? 0) -
        (state[`${a.id}:v${a.version}`]?.updatedAt ?? 0),
    );
  const unfinished = recent.find((item) => !completed(state, item.id));
  const next = unfinished ?? selectNextLesson(momentum.track, state);
  const checked = catalog.filter((item) => completed(state, item.id)).length;
  return (
    <>
      <div className="dashboard-heading">
        <div>
          <h1>Your workspace</h1>
          <p>
            {recent.length
              ? "Pick up your work, or follow a new idea."
              : "Choose a starting point. Make one idea work."}
          </p>
        </div>
        <Link className="dashboard-search" href="/problems/">
          <Search size={17} /> Find a lesson <ArrowRight size={15} />
        </Link>
      </div>
      <div className="dashboard-grid">
        <div className="dashboard-main">
          <section
            className="dashboard-next"
            aria-labelledby="next-heading"
            aria-busy={!ready}
          >
            <div className="dashboard-section-heading">
              <h2 id="next-heading">
                {unfinished ? "Continue learning" : "Your next lesson"}
              </h2>
              <span>{next?.difficulty ?? "Project"}</span>
            </div>
            <h3>{next?.title ?? "Put your skills to work"}</h3>
            <p>
              {next?.summary ??
                "You have checked your selected track. Connect the ideas in a retrieval system, or choose another path."}
            </p>
            <div className="dashboard-next-footer">
              <Link
                className="primary"
                href={next ? itemHref(next.id) : "/projects/mini-retrieval/"}
              >
                {unfinished
                  ? "Continue lesson"
                  : next
                    ? "Start lesson"
                    : "Open project"}
                <ArrowRight size={17} />
              </Link>
              {next && (
                <span>
                  <Clock3 size={14} /> {next.estimated_minutes} min{" "}
                  <span aria-hidden="true">·</span> {domains[next.domain]}
                </span>
              )}
            </div>
          </section>
          <section
            className="dashboard-paths"
            aria-labelledby="dashboard-paths-title"
          >
            <div className="dashboard-section-heading">
              <h2 id="dashboard-paths-title">Learning paths</h2>
              <Link
                className="text-link"
                href="/paths/"
                aria-label="Choose a learning path"
              >
                View all <ArrowRight size={14} />
              </Link>
            </div>
            <div className="dashboard-path-list">
              {paths.map((path, index) => {
                const done = path.items.filter((id) =>
                  completed(state, id),
                ).length;
                const Icon = pathIcons[index];
                return (
                  <Link
                    className={`dashboard-path path-tone-${index}`}
                    href={`/paths/${path.slug}/`}
                    key={path.slug}
                  >
                    <span className="dashboard-path-symbol">
                      <Icon size={23} strokeWidth={1.5} aria-hidden="true" />
                    </span>
                    <div>
                      <h3>{path.title}</h3>
                      <p>
                        {path.items.length} lessons{" "}
                        <span aria-hidden="true">·</span> {done} checked
                      </p>
                      <progress
                        aria-label={`${path.title} progress`}
                        max={path.items.length}
                        value={done}
                      />
                    </div>
                    <ArrowRight size={17} aria-hidden="true" />
                  </Link>
                );
              })}
            </div>
          </section>
          <section
            className="dashboard-tools"
            aria-label="Projects and experiments"
          >
            <Link
              href="/projects/mini-retrieval/"
              aria-label="Enter the project"
            >
              <FolderCode size={21} aria-hidden="true" />
              <div>
                <h2>Build a retrieval system</h2>
                <p>Bring the concepts together in a project.</p>
              </div>
              <ArrowRight size={17} />
            </Link>
            <Link href="/explore/" aria-label="Open the experiment lab">
              <FlaskConical size={21} aria-hidden="true" />
              <div>
                <h2>Try an experiment</h2>
                <p>Change a variable. See what follows.</p>
              </div>
              <ArrowRight size={17} />
            </Link>
          </section>
        </div>
        <aside className="dashboard-companion" aria-label="Personal learning">
          <div className="dashboard-completion">
            <span>
              <CheckCircle2 size={16} /> Your checked work
            </span>
            <p>
              <strong>{checked}</strong> / {catalog.length} lessons
            </p>
            <Link className="text-link" href="/progress/">
              View progress <ArrowRight size={14} />
            </Link>
          </div>
          <MomentumPanel compact />
          <section className="dashboard-beginner">
            <h2>A foundation to build on</h2>
            <p>
              18 selected lessons in real records, arrays, and small neural
              networks. Basic Python is enough to begin.
            </p>
            <Link className="text-link" href="/paths/start-here/">
              Follow the beginner route <ArrowRight size={15} />
            </Link>
          </section>
        </aside>
      </div>
      {recent.length > 0 && (
        <section className="dashboard-recent" aria-labelledby="recent-title">
          <div className="dashboard-section-heading">
            <h2 id="recent-title">Recently worked on</h2>
            <Link className="text-link" href="/progress/">
              All activity <ArrowRight size={14} />
            </Link>
          </div>
          <ul>
            {recent.slice(0, 3).map((item) => (
              <li key={item.id}>
                <Link href={itemHref(item.id)}>
                  <span>{item.title}</span>
                  <span>
                    {completed(state, item.id) ? "Checked" : "In progress"}
                    <ArrowRight size={15} />
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        </section>
      )}
    </>
  );
}
