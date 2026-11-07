import Link from "next/link";
import { LessonCatalog } from "@/components/learning";
import { LearningPage } from "@/components/learning-page";

export default function BeginnerLessonsPage() {
  return (
    <LearningPage title="Beginner lessons" active="practice">
      <h1>Build confidence with real problems.</h1>
      <p className="page-lead">
        Practice useful data transformations, numerical reasoning, and small
        model operations. Begin with the examples and use the hints when you
        need a starting point. You can change the filters to explore any level.
      </p>
      <p className="beginner-link">
        Prefer a short selection?{" "}
        <Link className="text-link" href="/paths/start-here/">
          Follow the beginner route.
        </Link>
      </p>
      <LessonCatalog initialLevel="beginner" />
    </LearningPage>
  );
}
