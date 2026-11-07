import { describe, expect, it } from "vitest";
import {
  MomentumSchema,
  defaultMomentum,
  localDay,
  weekStart,
  recordFirstCompletion,
  mergeMomentum,
  selectNextLesson,
  summarizeMomentum,
  quests,
} from "../../apps/web/src/lib/momentum";
import {
  allItems,
  beginnerTracks,
  catalog,
} from "../../apps/web/src/lib/curriculum";
import type { LearningState } from "../../apps/web/src/lib/progress";

const now = new Date(2026, 9, 31, 12);
const checked = (ids: string[], updatedAt = now.getTime()): LearningState =>
  Object.fromEntries(
    ids.map((id) => {
      const item = allItems.find((entry) => entry.id === id)!;
      return [
        `${id}:v${item.version}`,
        { completed: true, attempts: 1, updatedAt },
      ];
    }),
  );

describe("momentum dates and preferences", () => {
  it("starts with a voluntary goal and rejects malformed dates and settings", () => {
    expect(defaultMomentum()).toMatchObject({ enabled: true, weeklyTarget: 0 });
    expect(MomentumSchema.safeParse(defaultMomentum()).success).toBe(true);
    for (const patch of [
      { enabled: "true" },
      { weeklyTarget: 3 },
      { track: "unpublished-track" },
      { firstCompletions: { "m01:v1": "2026-02-29" } },
      { firstCompletions: { "m01:v1": "2026-04-31" } },
      { firstCompletions: { "m01:v1": "2026-10-31T12:00:00Z" } },
      { firstCompletions: { "m01:v0": "2026-10-31" } },
      { firstCompletions: { "../m01:v1": "2026-10-31" } },
      { firstCompletions: { "m01:v1": "0000-01-01" } },
    ]) {
      expect(
        MomentumSchema.safeParse({ ...defaultMomentum(), ...patch }).success,
      ).toBe(false);
    }
    expect(
      MomentumSchema.safeParse({
        ...defaultMomentum(),
        firstCompletions: { "m01:v1": "2024-02-29" },
      }).success,
    ).toBe(true);
  });

  it("uses local calendar boundaries across months, years and a DST weekend", () => {
    expect(localDay(new Date(2026, 9, 31, 23, 59))).toBe("2026-10-31");
    expect(weekStart(new Date(2027, 0, 1, 0, 1))).toBe("2026-12-28");
    expect(weekStart(new Date(2026, 10, 1, 23, 59))).toBe("2026-10-26");
    expect(weekStart(new Date(2026, 10, 2, 0, 0))).toBe("2026-11-02");
    expect(weekStart(new Date(2026, 2, 8, 12))).toBe("2026-03-02");
    expect(weekStart(new Date(2026, 2, 9, 12))).toBe("2026-03-09");
    expect(() => localDay(new Date("invalid"))).toThrow();
  });

  it("assigns a shared instant to the local week in India and across US daylight saving", () => {
    const previousTimezone = process.env.TZ;
    try {
      process.env.TZ = "Asia/Kolkata";
      const instant = new Date("2026-11-02T02:00:00Z");
      expect(localDay(instant)).toBe("2026-11-02");
      expect(weekStart(instant)).toBe("2026-11-02");
      process.env.TZ = "America/New_York";
      expect(localDay(instant)).toBe("2026-11-01");
      expect(weekStart(instant)).toBe("2026-10-26");
      expect(weekStart(new Date("2026-03-09T03:59:00Z"))).toBe("2026-03-02");
      expect(weekStart(new Date("2026-03-09T04:00:00Z"))).toBe("2026-03-09");
    } finally {
      if (previousTimezone === undefined) delete process.env.TZ;
      else process.env.TZ = previousTimezone;
    }
  });
});

describe("first-completion credit", () => {
  it("records a known version once without mutating or redating existing credit", () => {
    const initial = defaultMomentum();
    const first = recordFirstCompletion(initial, "m01", 1, now);
    expect(initial.firstCompletions).toEqual({});
    expect(first.firstCompletions).toEqual({ "m01:v1": "2026-10-31" });
    expect(recordFirstCompletion(first, "m01", 1, new Date(2026, 10, 2))).toBe(
      first,
    );
    expect(recordFirstCompletion(first, "m99999", 1, now)).toBe(first);
    expect(recordFirstCompletion(first, "m01", 999, now)).toBe(first);
  });

  it("counts legacy completions for all-time XP without inventing a completion week", () => {
    const state = checked(["m01", "m02", "p01"]);
    state["m99999:v1"] = {
      completed: true,
      updatedAt: now.getTime(),
      attempts: 9,
    };
    state["m03:v99"] = {
      completed: true,
      updatedAt: now.getTime(),
      attempts: 9,
    };
    state["m03:v1"] = {
      completed: false,
      updatedAt: now.getTime(),
      attempts: 100,
    };
    const summary = summarizeMomentum(state, defaultMomentum(), now);
    expect(summary).toMatchObject({
      xp: 50,
      lessonsCompleted: 2,
      projectsCompleted: 1,
      thisWeek: 0,
      level: 1,
      levelProgress: 50,
      xpToNextLevel: 50,
      goalReached: false,
    });
    const changedVisits = Object.fromEntries(
      Object.entries(state).map(([id, item]) => [
        id,
        { ...item, updatedAt: now.getTime() + 999999, attempts: 999 },
      ]),
    );
    expect(summarizeMomentum(changedVisits, defaultMomentum(), now)).toEqual(
      summary,
    );
  });

  it("includes this Monday and today, but excludes prior, future, unknown and project dates from the weekly lesson goal", () => {
    const momentum = {
      ...defaultMomentum(),
      weeklyTarget: 2 as const,
      firstCompletions: {
        "m01:v1": "2026-10-25",
        "m02:v1": "2026-10-26",
        "m03:v1": "2026-10-31",
        "m04:v1": "2026-11-01",
        "m05:v1": "2026-10-31",
        "p01:v1": "2026-10-31",
        "m99999:v1": "2026-10-31",
      },
    };
    const state = checked(["m01", "m02", "m03", "m04", "p01"]);
    expect(summarizeMomentum(state, momentum, now)).toMatchObject({
      thisWeek: 2,
      weekStart: "2026-10-26",
      goalReached: true,
    });
    const nextWeek = summarizeMomentum(state, momentum, new Date(2026, 10, 2));
    expect(nextWeek).toMatchObject({ thisWeek: 0, goalReached: false, xp: 70 });
    expect(
      summarizeMomentum(state, { ...momentum, weeklyTarget: 0 }, now)
        .goalReached,
    ).toBe(false);
  });

  it("crosses level and milestone boundaries once and caps the final lesson milestone", () => {
    const nine = summarizeMomentum(
      checked(catalog.slice(0, 9).map((item) => item.id)),
      defaultMomentum(),
      now,
    );
    expect(nine).toMatchObject({
      xp: 90,
      level: 1,
      levelProgress: 90,
      xpToNextLevel: 10,
      nextMilestone: 10,
    });
    const ten = summarizeMomentum(
      checked(catalog.slice(0, 10).map((item) => item.id)),
      defaultMomentum(),
      now,
    );
    expect(ten).toMatchObject({
      xp: 100,
      level: 2,
      levelProgress: 0,
      xpToNextLevel: 100,
      nextMilestone: 20,
    });
    const all = summarizeMomentum(
      checked(catalog.map((item) => item.id)),
      defaultMomentum(),
      now,
    );
    expect(all.nextMilestone).toBe(catalog.length);
    expect(all.milestoneProgress).toBe(10);
    expect(
      summarizeMomentum(
        checked(["m01"]),
        { ...defaultMomentum(), enabled: false },
        now,
      ).xp,
    ).toBe(10);
  });
});

describe("portable momentum", () => {
  it("merges earliest known dates idempotently, keeps device choices, and filters unsupported records", () => {
    const current = {
      ...defaultMomentum(),
      enabled: false,
      weeklyTarget: 4 as const,
      track: "deep-learning" as const,
      firstCompletions: { "m01:v1": "2026-10-30", "m02:v1": "2026-10-28" },
    };
    const incoming = {
      ...defaultMomentum(),
      weeklyTarget: 6 as const,
      firstCompletions: {
        "m01:v1": "2026-10-20",
        "m02:v1": "2026-10-31",
        "m03:v1": "2026-10-29",
        "m04:v1": "2026-11-01",
        "m05:v1": "2026-10-28",
        "m01:v2": "2026-10-29",
        "m99999:v1": "2026-10-29",
      },
    };
    const state = checked(["m01", "m02", "m03", "m04"]);
    const merged = mergeMomentum(current, incoming, state);
    expect(merged).toEqual({
      ...current,
      firstCompletions: {
        "m01:v1": "2026-10-20",
        "m02:v1": "2026-10-28",
        "m03:v1": "2026-10-29",
        "m04:v1": "2026-11-01",
      },
    });
    expect(mergeMomentum(merged, incoming, state)).toEqual(merged);
    expect(summarizeMomentum(state, merged, now).xp).toBe(40);
    expect(summarizeMomentum(state, merged, now).thisWeek).toBe(2);
    expect(current.firstCompletions["m01:v1"]).toBe("2026-10-30");
  });

  it("does not award current-week credit when an old backup contains only completions", () => {
    const state = checked(["m01"], now.getTime());
    const merged = mergeMomentum(defaultMomentum(), defaultMomentum(), state);
    expect(merged.firstCompletions).toEqual({});
    expect(summarizeMomentum(state, merged, now)).toMatchObject({
      xp: 10,
      thisWeek: 0,
    });
  });
});

describe("learning direction and earned milestones", () => {
  it("offers six real tracks and recommends unmet prerequisites before the selected lesson", () => {
    expect(quests).toHaveLength(6);
    expect(new Set(quests.map((quest) => quest.id)).size).toBe(6);
    for (const quest of quests) {
      for (const id of quest.items)
        expect(allItems.find((item) => item.id === id)).toBeDefined();
      const initial = selectNextLesson(quest.id, {});
      expect(initial).toBeDefined();
      expect(initial!.prerequisites).toHaveLength(0);
      expect(selectNextLesson(quest.id, checked(quest.items))).toBeUndefined();
    }
    expect(selectNextLesson("deep-learning", {})?.id).toBe("m01");
    expect(selectNextLesson("deep-learning", checked(["m01"]))?.id).toBe("m03");
    expect(selectNextLesson("deep-learning", checked(["m01", "m03"]))?.id).toBe(
      "d01",
    );
    expect(selectNextLesson("unknown", {})).toEqual(
      selectNextLesson("beginner-records", {}),
    );
  });

  it("earns track, domain and project milestones only from the required current completions", () => {
    const records = beginnerTracks[0].items;
    const almost = summarizeMomentum(
      checked(records.slice(0, -1)),
      defaultMomentum(),
      now,
    );
    expect(
      almost.achievements.find((item) => item.id === "beginner-records"),
    ).toMatchObject({
      earned: false,
      completed: records.length - 1,
      total: records.length,
    });
    const state = checked([...records, "m01", "d01", "p01"]);
    const summary = summarizeMomentum(state, defaultMomentum(), now);
    for (const id of [
      "first-check",
      "beginner-records",
      "three-domains",
      "project-builder",
    ])
      expect(summary.achievements.find((item) => item.id === id)?.earned).toBe(
        true,
      );
    expect(
      summary.achievements.find((item) => item.id === "beginner-arrays")
        ?.earned,
    ).toBe(false);
    expect(
      summary.achievements.every((item) => item.completed <= item.total),
    ).toBe(true);
  });
});
