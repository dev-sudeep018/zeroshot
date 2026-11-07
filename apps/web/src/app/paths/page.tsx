import { BeginnerEntry, PathList } from "@/components/learning";
import { LearningPage } from "@/components/learning-page";
export default function PathsPage() {
  return (
    <LearningPage title="Guided paths" active="paths">
      <h1>One idea builds on the next.</h1>
      <p className="page-lead">
        Read the explanation, change an experiment, then build the operation in
        Python. Prerequisites are helpful connections; you can enter wherever
        you are curious.
      </p>
      <BeginnerEntry />
      <PathList />
    </LearningPage>
  );
}
