import type { Metadata } from "next";
import "./globals.css";
import "./portal.css";
import "./marketing.css";
import "./auth.css";
import { AuthProvider } from "@/components/auth-provider";
export const metadata: Metadata = {
  title: "ZeroShot | Learn AI by building",
  description:
    "Free, open-source AI practice. Implement, experiment, and understand, one connected skill at a time.",
};
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <a className="skip-link" href="#main-content">
          Skip to content
        </a>
        <AuthProvider>{children}</AuthProvider>
      </body>
    </html>
  );
}
