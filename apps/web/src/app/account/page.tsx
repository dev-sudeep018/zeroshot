import type { Metadata } from "next";
import { Shell } from "@/components/shell";
import { AccountDetails } from "@/components/auth-form";

export const metadata: Metadata = { title: "Your account | ZeroShot" };

export default function AccountPage() {
  return (
    <Shell active="account">
      <header className="topbar">
        <span>Your account</span>
        <span className="free-label">Optional account · Free learning</span>
      </header>
      <div className="page-content account-content">
        <AccountDetails />
      </div>
    </Shell>
  );
}
