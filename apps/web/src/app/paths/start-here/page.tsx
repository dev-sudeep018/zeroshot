import { BeginnerGuide } from "@/components/learning";
import { LearningPage } from "@/components/learning-page";

export default function BeginnerRoutePage() {
  return (
    <LearningPage title="Beginner route" active="paths">
      <h1>Start small. Build something useful.</h1>
      <p className="page-lead">
        A selection of practical starting points for learners who know basic
        Python. Clean records, reason with measurements, and inspect how a model
        behaves. Choose a section that interests you; the full paths remain
        available whenever you want to go deeper.
      </p>
      <p className="muted">
        Read the examples, predict a result, then implement the operation. Hints
        help you take the next step. Your progress is shared with the lesson
        library and saved on this device.
      </p>
      <BeginnerGuide />
    </LearningPage>
  );
}
