"use client";
import Link from "next/link";
import { ArrowRight, CheckCircle2, Circle, Trophy } from "lucide-react";
import { completed } from "@/lib/progress";
import { itemHref } from "@/lib/curriculum";
import {
  quests,
  selectNextLesson,
  summarizeMomentum,
  type Momentum,
} from "@/lib/momentum";
import { useMomentum } from "@/lib/use-momentum";
import { useProgress } from "@/lib/use-progress";

export function MomentumPanel({ compact = false }: { compact?: boolean }) {
  const state = useProgress();
  const { momentum, ready, now, save, notice } = useMomentum();
  if (!ready || (compact && !momentum.enabled)) return null;
  const summary = summarizeMomentum(state, momentum, now);
  const quest =
    quests.find((entry) => entry.id === momentum.track) ?? quests[0];
  const next = selectNextLesson(quest.id, state);
  const done = quest.items.filter((id) => completed(state, id)).length;
  return (
    <section
      className={`momentum ${compact ? "momentum-compact" : ""}`}
      aria-label="Learning momentum"
    >
      <div className="momentum-heading">
        <h2>Learning momentum</h2>
        {compact ? (
          <Link className="text-link" href="/progress/#momentum">
            Choose your pace <ArrowRight size={15} />
          </Link>
        ) : (
          <label className="momentum-toggle">
            <input
              type="checkbox"
              checked={momentum.enabled}
              onChange={(event) => save({ enabled: event.target.checked })}
            />
            Show XP and milestones
          </label>
        )}
      </div>
      {!momentum.enabled ? (
        <p>
          Quiet mode is on. Your checked lessons and code stay saved. Turn this
          on whenever you want to see your practice rewards.
        </p>
      ) : (
        <>
          <div className="momentum-summary">
            <div className="momentum-level">
              <div>
                <strong>Practice level {summary.level}</strong>
                <p className="muted">
                  {summary.xp} XP · {summary.xpToNextLevel} to your next level
                </p>
                <progress
                  aria-label="Practice level progress"
                  max={100}
                  value={summary.levelProgress}
                />
              </div>
            </div>
            <div className="momentum-week">
              <strong>
                {summary.weeklyTarget
                  ? `${summary.thisWeek} / ${summary.weeklyTarget} lessons this week`
                  : "A pace that fits your week"}
              </strong>
              <p className={summary.goalReached ? "success-text" : "muted"}>
                {summary.goalReached
                  ? "Weekly goal reached. Take a break or follow your curiosity."
                  : summary.weeklyTarget
                    ? "Monday–Sunday, your local calendar. Your XP always stays."
                    : "Choose an optional weekly goal in your progress settings."}
              </p>
              {summary.weeklyTarget > 0 && (
                <progress
                  aria-label="Weekly lesson goal"
                  max={summary.weeklyTarget}
                  value={Math.min(summary.thisWeek, summary.weeklyTarget)}
                />
              )}
            </div>
          </div>
          {!compact && (
            <>
              <fieldset className="pace-options">
                <legend>Your weekly goal</legend>
                {[0, 2, 4, 6].map((target) => (
                  <label key={target}>
                    <input
                      type="radio"
                      name="weekly-goal"
                      value={target}
                      checked={momentum.weeklyTarget === target}
                      onChange={() =>
                        save({
                          weeklyTarget: target as Momentum["weeklyTarget"],
                        })
                      }
                    />
                    {target ? `${target} lessons` : "No goal"}
                  </label>
                ))}
              </fieldset>
              <p className="muted small">
                Change your goal at any time. Only first full-suite passes count
                this week. Earlier work without a recorded completion date
                counts toward XP, but not this week's goal.
              </p>
            </>
          )}
          <div className="momentum-quest">
            <div>
              <h3>{compact ? quest.title : "Your next learning quest"}</h3>
              {!compact && (
                <label className="quest-select">
                  Choose a focus
                  <select
                    value={momentum.track}
                    onChange={(event) =>
                      save({ track: event.target.value as Momentum["track"] })
                    }
                  >
                    {quests.map((entry) => (
                      <option key={entry.id} value={entry.id}>
                        {entry.title}
                      </option>
                    ))}
                  </select>
                </label>
              )}
              <p>
                {done} of {quest.items.length} checked ·{" "}
                {compact ? "One useful operation at a time." : quest.outcome}
              </p>
              {next && !quest.items.includes(next.id) && (
                <p className="info-text small">
                  Start with this supporting concept, then return to your chosen
                  track.
                </p>
              )}
            </div>
            <Link
              className="primary"
              href={next ? itemHref(next.id) : quest.href}
            >
              {next
                ? `Next: ${next.title}`
                : "Track checked — revisit your work"}
              <ArrowRight size={16} />
            </Link>
          </div>
          {!compact && (
            <>
              <div className="momentum-milestones">
                <h3>Milestones you can build on</h3>
                <p className="muted">
                  {summary.lessonsCompleted}{" "}
                  {summary.lessonsCompleted === 1 ? "lesson" : "lessons"}{" "}
                  checked.{" "}
                  {summary.lessonsCompleted >= summary.nextMilestone
                    ? "You've checked the whole published library."
                    : `Your next practice milestone is ${summary.nextMilestone}.`}
                </p>
                <ul>
                  {summary.achievements.map((badge) => (
                    <li key={badge.id}>
                      {badge.earned ? (
                        <Trophy
                          className="success-text"
                          size={20}
                          aria-hidden="true"
                        />
                      ) : (
                        <Circle
                          className="muted"
                          size={20}
                          aria-hidden="true"
                        />
                      )}
                      <div>
                        <Link href={badge.href}>{badge.title}</Link>
                        <p>{badge.description}</p>
                      </div>
                      <span className={badge.earned ? "success-text" : "muted"}>
                        {badge.earned ? (
                          <>
                            <CheckCircle2 size={15} /> Earned
                          </>
                        ) : (
                          `${badge.completed} / ${badge.total}`
                        )}
                      </span>
                    </li>
                  ))}
                </ul>
              </div>
              <details className="momentum-rules">
                <summary>How practice credit works</summary>
                <p>
                  Earn 10 XP once for each checked lesson and 30 XP for the
                  retrieval project checkpoint. All difficulty levels earn the
                  same lesson credit. Repeated checks, sample runs, and visits
                  add no XP. Each 100 XP marks a practice level.
                </p>
                <p>
                  XP records passed checks on the current published versions,
                  including reference-assisted work. It is not a measure of
                  expertise. To test your understanding, explain the result and
                  reconstruct the solution later without looking.
                </p>
                <p>
                  Everything stays on this device unless you export a backup.
                  Importing restores recorded work and dates; it never creates a
                  new completion today. Lessons stay open regardless of points,
                  pace, or milestones.
                </p>
              </details>
              <Link className="text-link" href="/problems/">
                Browse freely <ArrowRight size={15} />
              </Link>
            </>
          )}
        </>
      )}
      {!compact && (
        <p className="small muted" role="status">
          {notice}
        </p>
      )}
    </section>
  );
}
