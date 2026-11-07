import catalogData from "../generated/catalog.json";
import type { Problem } from "@zeroshot/problem-schema";

export const allItems = catalogData as unknown as Problem[];
export const catalog = allItems
  .filter((item) => item.kind !== "project")
  .sort((a, b) => {
    const order = ["foundations", "deep-learning", "engineering"];
    return (
      order.indexOf(a.domain) - order.indexOf(b.domain) ||
      a.id.localeCompare(b.id, "en", { numeric: true })
    );
  });
export const domains: Record<Problem["domain"], string> = {
  foundations: "Mathematics & ML",
  "deep-learning": "Deep learning",
  engineering: "AI engineering",
};
// Curated starting points reuse catalog lessons and their existing progress.
// They are not additional lessons or replacements for the three full paths.
export const beginnerTracks = [
  {
    title: "Work with real records",
    description:
      "Clean messy labels, reconcile requests, and organize records without losing information. You will use Python functions, loops, lists, and dictionaries.",
    items: ["e63", "e65", "e66", "e69", "e72", "e73"],
  },
  {
    title: "Reason with arrays and measurements",
    description:
      "Calibrate readings, handle missing observations, and summarize grids. Predict the output on a small example before writing the array operations.",
    items: ["m60", "m61", "m62", "m63", "m65", "m67"],
  },
  {
    title: "Understand a small neural network",
    description:
      "Count parameters, inspect activations, and follow training decisions. Small supplied arrays let you investigate one behavior at a time.",
    items: ["d80", "d84", "d85", "d90", "d95", "d100"],
  },
];
export const paths = [
  {
    slug: "mathematics-to-ml",
    title: "Mathematics to Machine Learning",
    description:
      "Connect probability, statistics, linear algebra, and classical machine learning to the behavior of a model.",
    outcome:
      "Reason about uncertainty, build numerical models, inspect clustering and statistical estimates, and compare policy objectives.",
    items: [
      "m01",
      "m02",
      "m03",
      "m04",
      "m05",
      "m06",
      "m07",
      "m08",
      "m09",
      "m10",
      "m11",
      "m12",
      "m13",
      "m14",
      "m15",
      "m16",
      "m17",
      "m18",
      "m19",
      ...Array.from({ length: 40 }, (_, index) => `m${index + 20}`),
      ...Array.from({ length: 100 }, (_, index) => `m${index + 60}`),
    ],
  },
  {
    slug: "deep-learning",
    title: "Deep Learning from First Principles",
    description:
      "Trace neural-network operations, recurrent state, structured predictions, generative models, and reinforcement learning.",
    outcome:
      "Check forward and backward passes, inspect attention and graph representations, and follow generative and reinforcement-learning updates.",
    items: [
      "d01",
      "d02",
      "d05",
      "d06",
      "d07",
      "d03",
      "d04",
      "d08",
      "d09",
      "d10",
      "d11",
      "d12",
      "d13",
      "d14",
      "d15",
      "d16",
      "d17",
      "d18",
      "d19",
      "d20",
      "d21",
      "d22",
      "d23",
      "d24",
      "d25",
      "d26",
      "d27",
      "d28",
      "d29",
      "d30",
      "d31",
      "d32",
      "d33",
      "d34",
      "d35",
      "d36",
      "d37",
      "d38",
      "d39",
      "d40",
      ...Array.from({ length: 39 }, (_, index) => `d${index + 41}`),
      ...Array.from({ length: 50 }, (_, index) => `d${index + 80}`),
    ],
  },
  {
    slug: "ai-engineering",
    title: "Practical AI Engineering",
    description:
      "Build text and retrieval operations, preserve data boundaries, evaluate uncertainty, and inspect inference and streaming systems.",
    outcome:
      "Evaluate evidence and predictions, detect distribution changes, and implement the small data and serving operations behind AI systems.",
    items: [
      "e01",
      "e02",
      "e05",
      "e03",
      "e04",
      "e06",
      "e07",
      "e08",
      "e09",
      "e10",
      "e11",
      "e12",
      "e13",
      "e14",
      "e15",
      "e16",
      "e17",
      "e18",
      "e19",
      "e20",
      "e21",
      "e22",
      ...Array.from({ length: 40 }, (_, index) => `e${index + 23}`),
      ...Array.from({ length: 100 }, (_, index) => `e${index + 63}`),
    ],
  },
];
export function itemById(id: string) {
  return allItems.find((item) => item.id === id);
}
export function itemHref(id: string) {
  return `/problems/${itemById(id)?.slug ?? ""}/`;
}
export function pathFor(id: string) {
  return paths.find((path) => path.items.includes(id));
}
