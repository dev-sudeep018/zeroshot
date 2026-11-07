import { Shell } from "./shell";
export function LearningPage({
  title,
  active,
  children,
}: {
  title: string;
  active: "home" | "practice" | "paths" | "explore" | "projects" | "progress";
  children: React.ReactNode;
}) {
  return (
    <Shell active={active}>
      <header className="topbar">
        <span className="portal-breadcrumb">
          <span>Learning portal</span>
          <span aria-hidden="true">/</span>
          <strong>{title}</strong>
        </span>
        <span className="free-label">Progress saved on this device</span>
      </header>
      <div className={`page-content learning-content surface-${active}`}>
        {children}
      </div>
    </Shell>
  );
}
