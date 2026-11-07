import { readFile } from "node:fs/promises";
import path from "node:path";
import type { LearningItem } from "@zeroshot/problem-schema";
import { allItems } from "./curriculum";

// Only called by server pages during static generation. Each route serializes
// its own lesson; the browser's catalog never includes every reference solution.
export async function loadItem(slug: string): Promise<LearningItem> {
  if (!allItems.some((item) => item.slug === slug))
    throw new Error("Unknown lesson");
  return JSON.parse(
    await readFile(
      path.join(process.cwd(), "src/generated/items", `${slug}.json`),
      "utf8",
    ),
  );
}
