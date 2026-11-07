import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight, ArrowUpRight } from "lucide-react";
import { PublicShell } from "@/components/public-shell";
import { catalog } from "@/lib/curriculum";

export const metadata: Metadata = {
  title: "About ZeroShot | Learning through the work",
};

export default function About() {
  return (
    <PublicShell active="about">
      <article className="public-about">
        <header className="public-about-intro">
          <h1>
            Understanding takes
            <br />
            <span>more than watching.</span>
          </h1>
          <p>
            ZeroShot is a free, open-source learning space for people who want
            to understand AI by working through the ideas themselves.
          </p>
        </header>
        <div className="public-about-layout">
          <aside className="public-about-aside">
            <p>
              Read a concept.
              <br />
              Try it in Python.
              <br />
              Inspect the result.
              <br />
              Build something with it.
            </p>
            <Link href="/learn/">
              Open the learning portal <ArrowRight size={16} />
            </Link>
          </aside>
          <div className="public-about-sections">
            <section>
              <h2>Learning through the work.</h2>
              <p>
                Every published lesson brings an explanation, examples, an
                incomplete starting point, hints, a reference solution, and
                executable checks together. Python and NumPy run on your device,
                in the browser.
              </p>
              <p>
                Guided paths give you structure. The lesson library and open lab
                give you room to follow your curiosity. A retrieval project
                connects individual operations into a small working system.
              </p>
              <p>
                The current curriculum contains {catalog.length} runnable
                lessons, three full learning paths, four interactive
                experiments, and one retrieval project. An 18-lesson beginner
                route offers a practical place to start.
              </p>
              <Link className="public-text-link" href="/paths/">
                Explore the guided paths <ArrowRight size={16} />
              </Link>
            </section>
            <section>
              <h2>Access without the setup.</h2>
              <p>
                The current curriculum needs no account, paid API key, GPU
                subscription, or payment. Basic Python is enough to begin the
                foundation route; each lesson explains the data and ML ideas it
                uses.
              </p>
              <p>
                Your drafts and progress are saved in this browser. You can
                export a backup and carry your work to another device. Account
                synchronization is a future milestone.
              </p>
            </section>
            <section>
              <h2>Open to use. Open to question.</h2>
              <p>
                Original software is licensed under Apache-2.0. Original
                educational writing is CC BY-SA 4.0. Adapted material retains
                its own attribution and license notices.
              </p>
              <p>
                The code, curriculum, and checks are available to inspect on
                GitHub. You can examine how a result is evaluated and contribute
                corrections where an explanation or implementation can be
                better.
              </p>
              <a
                className="public-text-link"
                href="https://github.com/dev-sudeep018/zeroshot"
                target="_blank"
                rel="noreferrer"
              >
                Explore the repository <ArrowUpRight size={16} />
              </a>
            </section>
            <section>
              <h2>Progress, with perspective.</h2>
              <p>
                A checked lesson records practice, not a professional
                credential. Optional XP, milestones, and flexible weekly goals
                make that work visible. They do not measure expertise or promise
                a job.
              </p>
              <p>
                The longer-term target is 2,000 reviewed learning problems.
                Today's published count reflects working lessons. More
                curriculum, projects, and learning tools are still ahead.
              </p>
            </section>
          </div>
        </div>
        <section className="public-start">
          <div>
            <h2>Start with a question.</h2>
            <p>The best way to understand the approach is to try it.</p>
          </div>
          <Link className="public-primary" href="/learn/">
            Start learning <ArrowRight size={18} />
          </Link>
        </section>
      </article>
    </PublicShell>
  );
}
