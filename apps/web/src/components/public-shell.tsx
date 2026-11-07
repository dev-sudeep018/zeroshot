import Link from "next/link";
import { ArrowRight, ArrowUpRight, Github } from "lucide-react";

export function PublicShell({
  children,
  active,
}: {
  children: React.ReactNode;
  active?: "about";
}) {
  return (
    <div className="public-site">
      <header className="public-header">
        <Link className="public-brand" href="/" aria-label="ZeroShot home">
          <svg viewBox="0 0 32 32" width="29" height="29" aria-hidden="true">
            <path
              d="M6 8h20L6 24h20M12 16h8"
              fill="none"
              stroke="currentColor"
              strokeWidth="2.5"
              strokeLinejoin="round"
            />
          </svg>
          <span>ZeroShot</span>
        </Link>
        <nav aria-label="Public navigation" className="public-nav">
          <Link href="/#how-it-works">How it works</Link>
          <Link href="/#curriculum">Curriculum</Link>
          <Link
            href="/about/"
            aria-current={active === "about" ? "page" : undefined}
          >
            About
          </Link>
          <Link href="/login/">Sign in</Link>
        </nav>
        <div className="public-header-actions">
          <a
            className="public-github"
            href="https://github.com/dev-sudeep018/zeroshot"
            target="_blank"
            rel="noreferrer"
            aria-label="ZeroShot on GitHub"
          >
            <Github size={19} />
          </a>
          <Link href="/learn/" className="public-enter">
            Open learning portal <ArrowUpRight size={16} />
          </Link>
        </div>
      </header>
      <main id="main-content">{children}</main>
      <footer className="public-footer">
        <div>
          <Link href="/" className="public-footer-wordmark">
            ZeroShot
          </Link>
          <p>Build the idea. Understand the result.</p>
        </div>
        <nav aria-label="Footer navigation">
          <Link href="/about/">About the project</Link>
          <a
            href="https://github.com/dev-sudeep018/zeroshot"
            target="_blank"
            rel="noreferrer"
          >
            Source on GitHub <ArrowUpRight size={14} />
          </a>
          <Link href="/learn/">
            Enter the portal <ArrowRight size={14} />
          </Link>
        </nav>
        <span className="public-footer-note">
          Free to learn. Open to inspect.
        </span>
      </footer>
    </div>
  );
}
