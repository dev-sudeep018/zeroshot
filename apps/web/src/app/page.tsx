import Link from "next/link";
import { ArrowRight, ArrowUpRight } from "lucide-react";
import { PublicShell } from "@/components/public-shell";
import { LearningPreview } from "@/components/landing";
import { catalog, paths } from "@/lib/curriculum";

const fields = [
  {
    title: "Mathematics into models.",
    description:
      "See what the equations are doing. Work with vectors, probability, statistics, and the numerical foundations behind a model.",
    topics: "Linear algebra · Probability · Classical ML",
    className: "math",
  },
  {
    title: "Inside the neural network.",
    description:
      "Follow the forward pass. Inspect a gradient. Build the operations behind attention, training, and representation learning.",
    topics: "Neural networks · Attention · Optimization",
    className: "neural",
  },
  {
    title: "AI that works with real data.",
    description:
      "Prepare records, retrieve evidence, and evaluate results. Connect the small engineering decisions that make a system useful.",
    topics: "Data operations · Retrieval · Evaluation",
    className: "engineering",
  },
];

export default function Home() {
  const beginnerCount = catalog.filter(
    (item) => item.difficulty === "beginner",
  ).length;
  return (
    <PublicShell>
      <div className="public-home">
        <section className="public-hero">
          <h1>
            Understand what
            <br />
            <span>makes AI work.</span>
          </h1>
          <div className="public-hero-copy">
            <p>
              Go from reading about a model to building the operations inside
              it. Learn through working code, small experiments, and the results
              you can explain.
            </p>
            <Link className="public-primary" href="/learn/">
              Start learning <ArrowRight size={18} />
            </Link>
            <span className="public-hero-note">
              Free and open source. No account needed.
            </span>
          </div>
        </section>
        <LearningPreview />
        <section
          className="public-curriculum"
          id="curriculum"
          aria-labelledby="curriculum-title"
        >
          <div className="public-section-heading">
            <h2 id="curriculum-title">A connected view of AI.</h2>
            <p>
              {catalog.length} runnable lessons across three fields. Follow a
              path from the foundations, or find the idea you want to
              understand.
            </p>
          </div>
          <div className="public-field-list">
            {paths.map((path, index) => (
              <Link
                href={`/paths/${path.slug}/`}
                className={`public-field public-field-${fields[index].className}`}
                key={path.slug}
              >
                <div className="public-field-figure" aria-hidden="true">
                  {index === 0 ? (
                    <svg viewBox="0 0 160 120" fill="none">
                      <path
                        d="M25 98h113M37 107V12"
                        stroke="currentColor"
                        opacity=".28"
                      />
                      <path
                        d="m37 98 80-58M37 98l38-71"
                        stroke="currentColor"
                        strokeWidth="2"
                      />
                      <path
                        d="m106 39 13-2-3 13M66 30l10-6 3 12"
                        stroke="currentColor"
                        strokeWidth="2"
                      />
                      <path d="M60 80a28 28 0 0 0-10-7" stroke="currentColor" />
                      <circle cx="37" cy="98" r="3" fill="currentColor" />
                    </svg>
                  ) : index === 1 ? (
                    <svg viewBox="0 0 160 120" fill="none">
                      <path
                        d="m30 28 50 32-50 32M30 28l50 0 50 32-50 32H30M80 28v64M80 60h50"
                        stroke="currentColor"
                        opacity=".35"
                      />
                      {[
                        [30, 28],
                        [30, 92],
                        [80, 28],
                        [80, 60],
                        [80, 92],
                        [130, 60],
                      ].map(([x, y]) => (
                        <circle
                          key={`${x}-${y}`}
                          cx={x}
                          cy={y}
                          r="7"
                          stroke="currentColor"
                          strokeWidth="1.5"
                          fill="#141b1c"
                        />
                      ))}
                    </svg>
                  ) : (
                    <svg viewBox="0 0 160 120" fill="none">
                      <path
                        d="M24 26h49v68H24zM87 40h49v40H87z"
                        stroke="currentColor"
                        strokeWidth="1.5"
                      />
                      <path
                        d="M34 40h27M34 51h27M34 62h18M34 80h27M99 52h25M99 64h16M73 60h14"
                        stroke="currentColor"
                        opacity=".6"
                      />
                      <path d="m82 55 5 5-5 5" stroke="currentColor" />
                    </svg>
                  )}
                </div>
                <div className="public-field-copy">
                  <h3>{fields[index].title}</h3>
                  <p>{fields[index].description}</p>
                  <span>{fields[index].topics}</span>
                </div>
                <div className="public-field-action">
                  <span>{path.items.length} lessons</span>
                  <ArrowUpRight size={23} />
                </div>
              </Link>
            ))}
          </div>
          <div className="public-beginner-note">
            <p>
              Know basic Python, but new to AI? Start with 18 selected lessons
              on records, arrays, and small neural networks. There are{" "}
              {beginnerCount} beginner lessons to explore as you grow.
            </p>
            <Link href="/paths/start-here/">
              Find your starting point <ArrowRight size={16} />
            </Link>
          </div>
        </section>
        <section className="public-project" aria-labelledby="project-title">
          <div className="public-project-copy">
            <h2 id="project-title">
              The pieces become
              <br />a working system.
            </h2>
            <p>
              Learning an operation is one thing. Knowing where it belongs is
              another. Build a small retrieval system that finds evidence,
              compares approaches, and makes the trade-offs visible.
            </p>
            <Link className="public-text-link" href="/projects/mini-retrieval/">
              Build the retrieval project <ArrowRight size={17} />
            </Link>
          </div>
          <ol className="public-project-stages">
            <li>
              <span>1</span>
              <div>
                <h3>Prepare the documents</h3>
                <p>Turn source text into useful chunks.</p>
              </div>
            </li>
            <li>
              <span>2</span>
              <div>
                <h3>Find the evidence</h3>
                <p>Compare keyword, vector, and hybrid retrieval.</p>
              </div>
            </li>
            <li>
              <span>3</span>
              <div>
                <h3>Evaluate what comes back</h3>
                <p>Look at the results. Explain the differences.</p>
              </div>
            </li>
          </ol>
        </section>
        <section className="public-start" aria-labelledby="start-title">
          <div>
            <h2 id="start-title">One idea is a good start.</h2>
            <p>
              Your learning space is ready. Pick a path, write some code, and
              see what happens.
            </p>
          </div>
          <Link href="/learn/" className="public-primary">
            Enter your learning space <ArrowRight size={18} />
          </Link>
        </section>
      </div>
    </PublicShell>
  );
}
