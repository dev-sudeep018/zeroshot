import { z } from "zod";
import { allItems as catalog } from "./curriculum";
import {
  MOMENTUM_KEY,
  MomentumSchema,
  defaultMomentum,
  mergeMomentum,
  recordFirstCompletion,
  type Momentum,
} from "./momentum";

// Keep the original keys so the ZeroShot rename preserves existing local work.
export const LEARNING_KEY = "mastery:learning:v1";
export const draftKey = (id: string, version: number) =>
  `mastery:draft:${id}:v${version}`;
export const completionKey = (id: string, version: number) =>
  `mastery:progress:${id}:v${version}`;
const firstCompletionKey = (id: string, version: number) =>
  `zeroshot:first-completion:${id}:v${version}`;
const recordSchema = z.strictObject({
  updatedAt: z.number().int().nonnegative().max(8_640_000_000_000_000),
  completed: z.boolean(),
  attempts: z.number().int().nonnegative().max(1_000_000),
});
const stateSchema = z.record(
  z.string().regex(/^[mdep][0-9]{2,5}:v[1-9][0-9]*$/),
  recordSchema,
);
export type LearningState = z.infer<typeof stateSchema>;
const keyFor = (id: string, version: number) => `${id}:v${version}`;
export function completed(state: LearningState, id: string) {
  const item = catalog.find((item) => item.id === id);
  return !!(item && state[keyFor(id, item.version)]?.completed);
}
export function readProgress(): LearningState {
  let state: LearningState = {};
  try {
    const parsed = stateSchema.safeParse(
      JSON.parse(localStorage.getItem(LEARNING_KEY) ?? "{}"),
    );
    if (parsed.success) state = parsed.data;
  } catch {
    // Completion markers remain useful if the aggregate cannot be decoded.
  }
  for (const item of catalog) {
    try {
      const key = keyFor(item.id, item.version);
      if (
        localStorage.getItem(completionKey(item.id, item.version)) ===
        "complete"
      )
        state[key] = {
          ...(state[key] ?? { updatedAt: 0, attempts: 0 }),
          completed: true,
        };
    } catch {
      // Preserve other readable records when a storage entry is unavailable.
    }
  }
  return state;
}
export function recordVisit(id: string, version: number, result?: boolean) {
  if (!catalog.some((item) => item.id === id && item.version === version))
    return false;
  const state = readProgress(),
    key = keyFor(id, version),
    previous = state[key];
  state[key] = {
    updatedAt: Date.now(),
    completed: !!previous?.completed || result === true,
    attempts: Math.min(
      1_000_000,
      (previous?.attempts ?? 0) + (result === undefined ? 0 : 1),
    ),
  };
  localStorage.setItem(LEARNING_KEY, JSON.stringify(state));
  if (state[key].completed)
    localStorage.setItem(completionKey(id, version), "complete");
  const firstPass = result === true && !previous?.completed;
  try {
    if (firstPass) {
      const momentum = recordFirstCompletion(readMomentum(), id, version);
      // Independent item keys survive simultaneous completions in other tabs.
      localStorage.setItem(
        firstCompletionKey(id, version),
        momentum.firstCompletions[key],
      );
      localStorage.setItem(MOMENTUM_KEY, JSON.stringify(momentum));
    }
  } finally {
    window.dispatchEvent(new Event("mastery-progress"));
  }
  return firstPass;
}
export function readMomentum(): Momentum {
  let momentum = defaultMomentum();
  try {
    const parsed = MomentumSchema.safeParse(
      JSON.parse(localStorage.getItem(MOMENTUM_KEY) ?? "null"),
    );
    if (parsed.success) momentum = parsed.data;
  } catch {
    // A malformed aggregate must not hide independent completion journals.
  }
  for (const item of catalog) {
    try {
      const key = keyFor(item.id, item.version);
      const date = localStorage.getItem(
        firstCompletionKey(item.id, item.version),
      );
      if (
        date &&
        MomentumSchema.safeParse({
          ...momentum,
          firstCompletions: { [key]: date },
        }).success
      ) {
        const old = momentum.firstCompletions[key];
        momentum.firstCompletions[key] = old && old < date ? old : date;
      }
    } catch {
      // Keep the aggregate and any readable journal entries if storage fails.
    }
  }
  return momentum;
}
export function saveMomentumPreferences(
  preferences: Pick<Momentum, "enabled" | "weeklyTarget" | "track">,
) {
  const next = MomentumSchema.parse({ ...readMomentum(), ...preferences });
  localStorage.setItem(MOMENTUM_KEY, JSON.stringify(next));
  window.dispatchEvent(new Event("mastery-progress"));
}
export function mergeProgress(
  current: LearningState,
  incoming: LearningState,
): LearningState {
  const merged = { ...current };
  for (const item of catalog) {
    const key = keyFor(item.id, item.version),
      next = incoming[key],
      prev = merged[key];
    if (next)
      merged[key] = {
        updatedAt: Math.max(prev?.updatedAt ?? 0, next.updatedAt),
        completed: !!prev?.completed || next.completed,
        attempts: Math.max(prev?.attempts ?? 0, next.attempts),
      };
  }
  return merged;
}
const backupFields = {
  progress: stateSchema,
  drafts: z.record(
    z.string().regex(/^mastery:draft:[mdep][0-9]{2,5}:v[1-9][0-9]*$/),
    z.string().max(32_000),
  ),
};
export const BackupSchema = z.union([
  z.strictObject({
    format: z.literal("project-mastery-backup"),
    version: z.literal(1),
    ...backupFields,
  }),
  z.strictObject({
    format: z.literal("zeroshot-backup"),
    version: z.literal(2),
    ...backupFields,
    momentum: MomentumSchema,
  }),
]);
export type Backup = z.infer<typeof BackupSchema>;
export function exportBackup(): Backup {
  const drafts: Record<string, string> = {};
  for (const item of catalog) {
    const key = draftKey(item.id, item.version);
    try {
      const value = JSON.parse(localStorage.getItem(key) ?? "null");
      if (
        value?.version === 1 &&
        typeof value.code === "string" &&
        value.code.length <= 32_000
      )
        drafts[key] = value.code;
    } catch {
      /* A corrupt draft must not prevent the remaining export. */
    }
  }
  return {
    format: "zeroshot-backup",
    version: 2,
    progress: readProgress(),
    drafts,
    momentum: readMomentum(),
  };
}
export function importBackup(backup: Backup) {
  const valid = BackupSchema.parse(backup);
  const progress = mergeProgress(readProgress(), valid.progress);
  const currentMomentum = readMomentum();
  // Restore preferences on a new device; preserve choices on an existing one.
  const base =
    valid.version === 2 && localStorage.getItem(MOMENTUM_KEY) === null
      ? valid.momentum
      : currentMomentum;
  localStorage.setItem(LEARNING_KEY, JSON.stringify(progress));
  const momentum = mergeMomentum(
    base,
    valid.version === 2 ? valid.momentum : defaultMomentum(),
    progress,
  );
  localStorage.setItem(MOMENTUM_KEY, JSON.stringify(momentum));
  for (const item of catalog) {
    const day = momentum.firstCompletions[keyFor(item.id, item.version)];
    if (day)
      localStorage.setItem(firstCompletionKey(item.id, item.version), day);
    if (progress[keyFor(item.id, item.version)]?.completed)
      localStorage.setItem(completionKey(item.id, item.version), "complete");
    const key = draftKey(item.id, item.version);
    if (valid.drafts[key] !== undefined && localStorage.getItem(key) === null)
      localStorage.setItem(
        key,
        JSON.stringify({ version: 1, code: valid.drafts[key] }),
      );
  }
  window.dispatchEvent(new Event("mastery-progress"));
}
