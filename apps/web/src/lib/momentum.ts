import { z } from "zod";
import { allItems, beginnerTracks, catalog, paths } from "./curriculum";
import type { LearningState } from "./progress";

export const MOMENTUM_KEY = "zeroshot:momentum:v1";
const trackIds = [
  "beginner-records",
  "beginner-arrays",
  "beginner-neural",
  "mathematics-to-ml",
  "deep-learning",
  "ai-engineering",
] as const;

// Store calendar dates, not UTC timestamps: a weekly goal follows the local
// calendar on which the work was completed, even after travel or a DST change.
const daySchema = z
  .string()
  .regex(/^\d{4}-\d{2}-\d{2}$/)
  .refine((value) => {
    const [year, month, day] = value.split("-").map(Number);
    if (year < 1 || month < 1 || month > 12 || day < 1) return false;
    const date = new Date(0);
    date.setUTCFullYear(year, month - 1, day);
    return (
      date.getUTCFullYear() === year &&
      date.getUTCMonth() === month - 1 &&
      date.getUTCDate() === day
    );
  }, "Use a valid calendar date.");

export const MomentumSchema = z.strictObject({
  enabled: z.boolean(),
  weeklyTarget: z.union([
    z.literal(0),
    z.literal(2),
    z.literal(4),
    z.literal(6),
  ]),
  track: z.enum(trackIds),
  firstCompletions: z
    .record(z.string().regex(/^[mdep][0-9]{2,5}:v[1-9][0-9]{0,8}$/), daySchema)
    .refine(
      (entries) => Object.keys(entries).length <= 10_000,
      "Too many completion records.",
    ),
});
export type Momentum = z.infer<typeof MomentumSchema>;

export function defaultMomentum(): Momentum {
  return {
    enabled: true,
    weeklyTarget: 0,
    track: "beginner-records",
    firstCompletions: {},
  };
}

export function localDay(date: Date): string {
  if (!Number.isFinite(date.getTime())) throw new RangeError("Invalid date.");
  const value = `${String(date.getFullYear()).padStart(4, "0")}-${String(date.getMonth() + 1).padStart(2, "0")}-${String(date.getDate()).padStart(2, "0")}`;
  return daySchema.parse(value);
}

export function weekStart(date: Date): string {
  const monday = new Date(date);
  monday.setHours(12, 0, 0, 0);
  monday.setDate(monday.getDate() - ((monday.getDay() + 6) % 7));
  return localDay(monday);
}

export const quests = [
  ...beginnerTracks.map((track, index) => ({
    id: trackIds[index],
    title: track.title,
    items: track.items,
    outcome: track.description,
    href: "/paths/start-here/",
  })),
  ...paths.map((path) => ({
    id: path.slug,
    title: path.title,
    items: path.items,
    outcome: path.outcome,
    href: `/paths/${path.slug}/`,
  })),
];

const keyFor = (id: string, version: number) => `${id}:v${version}`;
function isComplete(state: LearningState, id: string): boolean {
  const item = allItems.find((entry) => entry.id === id);
  return !!item && state[keyFor(id, item.version)]?.completed === true;
}

/** Call only when an incomplete item first passes its entire public test suite. */
export function recordFirstCompletion(
  momentum: Momentum,
  id: string,
  version: number,
  date = new Date(),
): Momentum {
  const item = allItems.find(
    (entry) => entry.id === id && entry.version === version,
  );
  const key = keyFor(id, version);
  if (!item || momentum.firstCompletions[key]) return momentum;
  return {
    ...momentum,
    firstCompletions: { ...momentum.firstCompletions, [key]: localDay(date) },
  };
}

/** Import dates only for known completed versions; importing is not new work. */
export function mergeMomentum(
  current: Momentum,
  incoming: Momentum,
  validProgress: LearningState,
): Momentum {
  const firstCompletions: Record<string, string> = {};
  // A source device may already be on tomorrow's calendar date. Preserve its
  // valid history here; the summary decides when it belongs to the local week.
  for (const item of allItems) {
    const key = keyFor(item.id, item.version);
    if (!validProgress[key]?.completed) continue;
    const dates = [
      current.firstCompletions[key],
      incoming.firstCompletions[key],
    ]
      .filter((date) => date !== undefined && daySchema.safeParse(date).success)
      .sort();
    if (dates.length) firstCompletions[key] = dates[0];
  }
  return { ...current, firstCompletions };
}

/** Recommendations never lock access: suggest an unmet prerequisite first. */
export function selectNextLesson(trackId: string, state: LearningState) {
  const quest = quests.find((entry) => entry.id === trackId) ?? quests[0];
  const seen = new Set<string>();
  function next(id: string): (typeof allItems)[number] | undefined {
    if (seen.has(id) || isComplete(state, id)) return undefined;
    seen.add(id);
    const item = allItems.find((entry) => entry.id === id);
    if (!item) return undefined;
    for (const prerequisite of item.prerequisites) {
      const pending = next(prerequisite);
      if (pending) return pending;
    }
    return item;
  }
  for (const id of quest.items) {
    const item = next(id);
    if (item) return item;
  }
  return undefined;
}

export function summarizeMomentum(
  state: LearningState,
  momentum: Momentum,
  now = new Date(),
) {
  const lessons = catalog.filter((item) => isComplete(state, item.id));
  const projects = allItems.filter(
    (item) => item.kind === "project" && isComplete(state, item.id),
  );
  const xp = lessons.length * 10 + projects.length * 30;
  const today = localDay(now),
    start = weekStart(now);
  const thisWeek = lessons.filter((item) => {
    const date = momentum.firstCompletions[keyFor(item.id, item.version)];
    return (
      date !== undefined &&
      daySchema.safeParse(date).success &&
      date >= start &&
      date <= today
    );
  }).length;
  const achievement = (
    id: string,
    title: string,
    description: string,
    count: number,
    total: number,
    href: string,
  ) => ({
    id,
    title,
    description,
    completed: Math.min(count, total),
    total,
    earned: count >= total,
    href,
  });
  const achievements = [
    achievement(
      "first-check",
      "First checked lesson",
      "Pass the full test suite for one lesson.",
      lessons.length,
      1,
      "/problems/",
    ),
    ...beginnerTracks.map((track, index) =>
      achievement(
        trackIds[index],
        track.title,
        `Check all ${track.items.length} lessons in this starter track.`,
        track.items.filter((id) => isComplete(state, id)).length,
        track.items.length,
        "/paths/start-here/",
      ),
    ),
    achievement(
      "three-domains",
      "Explore three fields",
      "Check a lesson in mathematics, deep learning, and AI engineering.",
      new Set(lessons.map((item) => item.domain)).size,
      3,
      "/paths/",
    ),
    achievement(
      "project-builder",
      "Connect a project",
      "Pass the retrieval project's full test suite.",
      isComplete(state, "p01") ? 1 : 0,
      1,
      "/projects/mini-retrieval/",
    ),
  ];
  return {
    xp,
    level: Math.floor(xp / 100) + 1,
    levelProgress: xp % 100,
    xpToNextLevel: 100 - (xp % 100),
    lessonsCompleted: lessons.length,
    projectsCompleted: projects.length,
    thisWeek,
    weekStart: start,
    weeklyTarget: momentum.weeklyTarget,
    goalReached: momentum.weeklyTarget > 0 && thisWeek >= momentum.weeklyTarget,
    nextMilestone: Math.min(
      catalog.length,
      (Math.floor(lessons.length / 10) + 1) * 10,
    ),
    milestoneProgress:
      lessons.length === catalog.length ? 10 : lessons.length % 10,
    achievements,
  };
}
