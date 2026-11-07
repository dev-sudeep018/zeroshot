import Link from "next/link";
import { LessonCatalog } from "@/components/learning";
import { LearningPage } from "@/components/learning-page";
export default function LessonsPage() {
  return (
    <LearningPage title="Lesson library" active="practice">
      <h1>Find the idea you need.</h1>
      <p className="page-lead">
        Explore a concept, inspect its behavior, and build it. Every published
        lesson includes a working reference and public checks.
      </p>
      <p className="beginner-link">
        Building your foundations?{" "}
        <Link className="text-link" href="/beginner/">
          Explore beginner lessons.
        </Link>
      </p>
      <LessonCatalog />
    </LearningPage>
  );
}
