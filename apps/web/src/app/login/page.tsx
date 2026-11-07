import Link from "next/link";
import type { Metadata } from "next";
import { ArrowLeft } from "lucide-react";
import { AuthForm } from "@/components/auth-form";

export const metadata: Metadata = { title: "Sign in | ZeroShot" };

export default function LoginPage() {
  return (
    <div className="auth-page">
      <header className="auth-header">
        <Link className="auth-wordmark" href="/" aria-label="ZeroShot website">
          <svg
            width="27"
            height="27"
            viewBox="0 0 28 28"
            fill="none"
            aria-hidden="true"
          >
            <path
              d="M4 5H24L4 23H24M11 14H17"
              stroke="currentColor"
              strokeWidth="2.5"
              strokeLinejoin="round"
            />
          </svg>
          ZeroShot
        </Link>
        <Link className="text-link" href="/learn/">
          <ArrowLeft size={15} /> Learning portal
        </Link>
      </header>
      <main id="main-content" className="auth-main">
        <AuthForm />
      </main>
      <footer className="auth-footer">Free to learn. Open to everyone.</footer>
    </div>
  );
}
