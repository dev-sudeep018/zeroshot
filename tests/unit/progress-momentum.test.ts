import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import {
  BackupSchema,
  exportBackup,
  importBackup,
  LEARNING_KEY,
  readMomentum,
  readProgress,
  recordVisit,
  saveMomentumPreferences,
} from "../../apps/web/src/lib/progress";
import {
  MOMENTUM_KEY,
  summarizeMomentum,
} from "../../apps/web/src/lib/momentum";

beforeEach(() => {
  const store = new Map<string, string>();
  vi.stubGlobal("localStorage", {
    getItem: (key: string) => store.get(key) ?? null,
    setItem: (key: string, value: string) => store.set(key, value),
    removeItem: (key: string) => store.delete(key),
    clear: () => store.clear(),
  });
  vi.stubGlobal("window", new EventTarget());
});
afterEach(() => {
  vi.unstubAllGlobals();
  vi.useRealTimers();
});

describe("progress and reward persistence", () => {
  it("recovers completion markers after malformed progress JSON without crediting a legacy pass again", () => {
    localStorage.setItem(LEARNING_KEY, "broken");
    localStorage.setItem("mastery:progress:m02:v1", "complete");
    localStorage.setItem("mastery:progress:e01:v1", "complete");
    localStorage.setItem("mastery:progress:m03:v1", "invalid");
    expect(readProgress()).toEqual({
      "m02:v1": { completed: true, updatedAt: 0, attempts: 0 },
      "e01:v1": { completed: true, updatedAt: 0, attempts: 0 },
    });
    expect(recordVisit("m02", 1, true)).toBe(false);
    expect(readMomentum().firstCompletions).toEqual({});
    expect(summarizeMomentum(readProgress(), readMomentum())).toMatchObject({
      xp: 20,
      thisWeek: 0,
    });
    expect(readProgress()["e01:v1"].completed).toBe(true);
  });

  it("recovers completion journals when aggregate JSON is malformed", () => {
    recordVisit("m02", 1, true);
    recordVisit("e01", 1, true);
    const dates = readMomentum().firstCompletions;
    localStorage.setItem(MOMENTUM_KEY, "broken");
    localStorage.setItem("zeroshot:first-completion:m03:v1", "2026-02-30");
    expect(readMomentum().firstCompletions).toEqual(dates);
    expect(summarizeMomentum(readProgress(), readMomentum())).toMatchObject({
      xp: 20,
      thisWeek: 2,
    });
  });

  it("preserves a valid source date across timezone backup transfers until it becomes locally eligible", () => {
    const previousTimezone = process.env.TZ;
    vi.useFakeTimers();
    try {
      vi.setSystemTime(new Date("2026-11-01T19:00:00Z"));
      process.env.TZ = "Asia/Kolkata";
      recordVisit("m02", 1, true);
      const backup = exportBackup();
      process.env.TZ = "America/New_York";
      localStorage.clear();
      importBackup(backup);
      expect(readMomentum().firstCompletions["m02:v1"]).toBe("2026-11-02");
      expect(summarizeMomentum(readProgress(), readMomentum())).toMatchObject({
        xp: 10,
        thisWeek: 0,
      });
      const roundTrip = exportBackup();
      localStorage.clear();
      importBackup(roundTrip);
      expect(readMomentum().firstCompletions["m02:v1"]).toBe("2026-11-02");
      vi.setSystemTime(new Date("2026-11-02T17:00:00Z"));
      expect(summarizeMomentum(readProgress(), readMomentum())).toMatchObject({
        xp: 10,
        thisWeek: 1,
      });
    } finally {
      if (previousTimezone === undefined) delete process.env.TZ;
      else process.env.TZ = previousTimezone;
    }
  });

  it("recovers both dated completions when a second tab overwrites the aggregate snapshot", () => {
    recordVisit("m02", 1, true);
    const staleProgress = localStorage.getItem(LEARNING_KEY)!;
    const staleMomentum = localStorage.getItem(MOMENTUM_KEY)!;
    recordVisit("e01", 1, true);
    localStorage.setItem(LEARNING_KEY, staleProgress);
    localStorage.setItem(MOMENTUM_KEY, staleMomentum);
    expect(summarizeMomentum(readProgress(), readMomentum())).toMatchObject({
      xp: 20,
      thisWeek: 2,
    });
    expect(Object.keys(readMomentum().firstCompletions)).toHaveLength(2);
  });
  it("credits only the first full success, preserving attempts and first date", () => {
    recordVisit("m02", 1);
    recordVisit("m02", 1, false);
    expect(summarizeMomentum(readProgress(), readMomentum()).xp).toBe(0);
    expect(recordVisit("m02", 1, true)).toBe(true);
    const dated = readMomentum();
    expect(recordVisit("m02", 1, true)).toBe(false);
    recordVisit("m02", 1, false);
    expect(readMomentum()).toEqual(dated);
    expect(readProgress()["m02:v1"].attempts).toBe(4);
    expect(summarizeMomentum(readProgress(), dated)).toMatchObject({
      xp: 10,
      thisWeek: 1,
    });
    expect(recordVisit("m99999", 1, true)).toBe(false);
  });
  it("keeps legacy completion credit without inventing a first-pass date", () => {
    localStorage.setItem("mastery:progress:m02:v1", "complete");
    expect(recordVisit("m02", 1, true)).toBe(false);
    expect(readMomentum().firstCompletions).toEqual({});
    expect(summarizeMomentum(readProgress(), readMomentum())).toMatchObject({
      xp: 10,
      thisWeek: 0,
    });
  });
  it("round trips v2 preferences/dates/drafts and merges repeatedly without farming credit", () => {
    recordVisit("m02", 1, true);
    saveMomentumPreferences({
      enabled: false,
      weeklyTarget: 4,
      track: "deep-learning",
    });
    localStorage.setItem(
      "mastery:draft:m02:v1",
      JSON.stringify({ version: 1, code: "# saved" }),
    );
    const backup = exportBackup();
    expect(backup).toMatchObject({ format: "zeroshot-backup", version: 2 });
    localStorage.clear();
    importBackup(backup);
    expect(readMomentum()).toMatchObject({
      enabled: false,
      weeklyTarget: 4,
      track: "deep-learning",
    });
    saveMomentumPreferences({
      enabled: true,
      weeklyTarget: 2,
      track: "beginner-records",
    });
    localStorage.setItem(
      "mastery:draft:m02:v1",
      JSON.stringify({ version: 1, code: "# keep" }),
    );
    importBackup(backup);
    importBackup(backup);
    expect(readMomentum()).toMatchObject({ enabled: true, weeklyTarget: 2 });
    expect(summarizeMomentum(readProgress(), readMomentum())).toMatchObject({
      xp: 10,
      thisWeek: 1,
    });
    expect(JSON.parse(localStorage.getItem("mastery:draft:m02:v1")!).code).toBe(
      "# keep",
    );
  });
  it("accepts the previous brand's backup and recovers from malformed reward storage", () => {
    localStorage.setItem(MOMENTUM_KEY, "broken");
    expect(readMomentum().weeklyTarget).toBe(0);
    importBackup(
      BackupSchema.parse({
        format: "project-mastery-backup",
        version: 1,
        progress: {
          "m02:v1": { completed: true, updatedAt: Date.now(), attempts: 1 },
        },
        drafts: {},
      }),
    );
    expect(summarizeMomentum(readProgress(), readMomentum())).toMatchObject({
      xp: 10,
      thisWeek: 0,
    });
    expect(localStorage.getItem(LEARNING_KEY)).toContain("m02:v1");
  });
});
