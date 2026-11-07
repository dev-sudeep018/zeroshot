import type { Metadata } from "next";
import { LearningDashboard } from "@/components/learning-dashboard";
import { LearningPage } from "@/components/learning-page";

export const metadata: Metadata = { title: "Learning home · ZeroShot" };
export default function LearnPage() {
  return (
    <LearningPage title="Home" active="home">
      <LearningDashboard />
    </LearningPage>
  );
}
