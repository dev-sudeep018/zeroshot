# ZeroShot

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Confirmed in the supplied founding plan: Next.js App Router, TypeScript, pnpm workspaces, Monaco, Pyodide and NumPy, versioned YAML/Markdown/Python content. Static frontend with a separately hosted, sandboxed runner. Optional Firebase Authentication provides email/password accounts on the free Spark plan. Learning data remains local until account synchronization is implemented.

## Users

Python programmers developing AI foundations and practical engineering skills. The founder leads product direction and delegates implementation to Codex.

## Product Purpose

Free, open-source practice that connects concepts, implementation, feedback, and integrated projects. Completion demonstrates practice, not independently verified certification or a job guarantee.

## Operating Context

Three connected entry points: guided learning, project-first learning, and open exploration. A learner can understand a concept, experiment with it, practise an implementation, interpret feedback, and use it in a project. Desktop coding and responsive reading. No sign-up, paid API, or hosted GPU requirement for the introductory curriculum.

## Capabilities and Constraints

The founder's content target is 2,000 problems and learning activities. The platform must not imitate a LeetCode problem queue. The current 450 lessons include 205 beginner lessons and two debugging investigations, with three full paths, a curated beginner route, and a mini retrieval project. They establish reusable learning formats, not the final product size. All three entry points share content and progress.

Only implemented and validated activities count as available. Planned content and generated variants must not be presented as 2,000 distinct completed lessons. Per-item content and evaluators load on demand so the browser does not download the whole curriculum.

Learner code must not access application credentials. Workers alone are not the isolation boundary. Content, reference solutions, schema, and runtime behavior require automated validation. Git and GitHub provide version control, review, and CI.

## Brand Commitments

ZeroShot is the project name, with no OpenAI affiliation. The latest user direction requires a dark public website separate from the learning portal. The landing page and About explain the product; /learn/ and the existing lesson, path, project, lab, and progress routes form a task-focused portal. Charcoal surfaces, warm off-white type, and restrained seafoam actions replace the rejected light design. Semantic green success, red errors, amber warnings, and blue information remain paired with labels. Local Manrope typography, accessible controls, and resizable editor panels remain requirements.

## Evidence on Hand

The supplied founding conversation establishes scope and decisions. No user counts, learning outcomes, client names, or employment results have been demonstrated.

## Product Principles

Free learning; explanations and experiments before scoring; connected projects; depth before quantity; browser/local computation; reproducible content; contributor-friendly architecture. Avoid competitive rankings, speed pressure, or accepted/rejected feedback as the organizing experience.

## Open Decisions

Public launch date, production hosting, and account synchronization remain later decisions.

## Personal learning momentum

Optional practice XP, milestones, a chosen track, and flexible weekly goals support the learning loop. No competitive rankings or daily penalties. XP records checked practice on current lesson versions, not expertise. See [the evidence and implementation plan](docs/research/gamification-evidence.md). Existing local storage and legacy backups survive the ZeroShot rename.
