"use client";
import { useEffect, useState } from "react";
import { defaultMomentum, type Momentum } from "./momentum";
import { readMomentum, saveMomentumPreferences } from "./progress";

export function useMomentum() {
  const [momentum, setMomentum] = useState(defaultMomentum);
  const [ready, setReady] = useState(false);
  const [now, setNow] = useState(() => new Date());
  const [notice, setNotice] = useState("");
  useEffect(() => {
    const refresh = () => {
      setMomentum(readMomentum());
      setNow(new Date());
      setReady(true);
    };
    refresh();
    addEventListener("storage", refresh);
    addEventListener("mastery-progress", refresh);
    document.addEventListener("visibilitychange", refresh);
    const timer = setInterval(refresh, 60_000);
    return () => {
      removeEventListener("storage", refresh);
      removeEventListener("mastery-progress", refresh);
      document.removeEventListener("visibilitychange", refresh);
      clearInterval(timer);
    };
  }, []);
  function save(
    patch: Partial<Pick<Momentum, "enabled" | "weeklyTarget" | "track">>,
  ) {
    try {
      saveMomentumPreferences({ ...readMomentum(), ...patch });
      setNotice("Preferences saved on this device.");
    } catch {
      setNotice(
        "Could not save preferences. Browser storage may be full or unavailable.",
      );
    }
  }
  return { momentum, ready, now, save, notice };
}
