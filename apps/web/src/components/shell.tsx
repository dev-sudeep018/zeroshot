"use client";
import Link from "next/link";
import { useState } from "react";
import {
  ArrowUpRight,
  BookOpen,
  FlaskConical,
  FolderCode,
  Github,
  House,
  Menu,
  Route,
  TrendingUp,
  UserRound,
  X,
} from "lucide-react";

const navigation = [
  { key: "home", href: "/learn/", label: "Learning home", icon: House },
  {
    key: "practice",
    href: "/problems/",
    label: "Lesson library",
    icon: BookOpen,
  },
  { key: "paths", href: "/paths/", label: "Guided paths", icon: Route },
  {
    key: "projects",
    href: "/projects/mini-retrieval/",
    label: "Projects",
    icon: FolderCode,
  },
  { key: "explore", href: "/explore/", label: "Open lab", icon: FlaskConical },
  {
    key: "progress",
    href: "/progress/",
    label: "Your progress",
    icon: TrendingUp,
  },
] as const;

export function Shell({
  children,
  active = "practice",
  workspace = false,
}: {
  children: React.ReactNode;
  active?:
    | "home"
    | "practice"
    | "paths"
    | "explore"
    | "projects"
    | "progress"
    | "about"
    | "account";
  workspace?: boolean;
}) {
  const [menuOpen, setMenuOpen] = useState(false);
  return (
    <div
      className={`app-shell portal-shell ${workspace ? "workspace-shell" : ""}`}
    >
      <aside className="portal-navigation" aria-label="Learning portal">
        <div className="portal-brand-row">
          <Link className="portal-brand" href="/learn/" aria-label="ZeroShot">
            <svg
              width="27"
              height="27"
              viewBox="0 0 28 28"
              fill="none"
              aria-hidden="true"
            >
              <path
                d="M4 5H24L4 23H24"
                stroke="currentColor"
                strokeWidth="2.5"
                strokeLinejoin="round"
              />
              <path d="M11 14H17" stroke="currentColor" strokeWidth="2.5" />
            </svg>
            <span>ZeroShot</span>
          </Link>
          <button
            className="portal-menu-toggle"
            aria-label="Toggle learning navigation"
            aria-expanded={menuOpen}
            aria-controls="portal-menu"
            onClick={() => setMenuOpen(!menuOpen)}
          >
            {menuOpen ? <X size={20} /> : <Menu size={20} />}
          </button>
        </div>
        <div
          id="portal-menu"
          className={`portal-menu ${menuOpen ? "is-open" : ""}`}
          onKeyDown={(event) => {
            if (event.key === "Escape") {
              setMenuOpen(false);
              document
                .querySelector<HTMLButtonElement>(".portal-menu-toggle")
                ?.focus();
            }
          }}
        >
          <nav aria-label="Main navigation">
            {navigation.map(({ key, href, label, icon: Icon }) => (
              <Link
                key={key}
                href={href}
                aria-current={active === key ? "page" : undefined}
                onClick={() => setMenuOpen(false)}
              >
                <Icon size={18} strokeWidth={1.6} aria-hidden="true" />
                <span>{label}</span>
              </Link>
            ))}
          </nav>
          <div className="portal-support">
            <Link href="/paths/start-here/" className="portal-start-link">
              <span>New to AI?</span>
              <strong>
                Start with the foundations <ArrowUpRight size={15} />
              </strong>
            </Link>
            <div className="portal-exit-links">
              <Link
                href="/account/"
                aria-current={active === "account" ? "page" : undefined}
              >
                <UserRound size={15} /> Your account
              </Link>
              <Link href="/">
                ZeroShot website <ArrowUpRight size={14} />
              </Link>
              <a
                href="https://github.com/dev-sudeep018/zeroshot"
                target="_blank"
                rel="noreferrer"
                aria-label="Build with us on GitHub"
              >
                <Github size={15} /> GitHub <ArrowUpRight size={14} />
              </a>
            </div>
          </div>
        </div>
      </aside>
      <main id="main-content" className="main-area">
        {children}
      </main>
    </div>
  );
}
