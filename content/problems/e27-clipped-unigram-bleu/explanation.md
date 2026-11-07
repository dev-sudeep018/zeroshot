# Explore Clipping and Brevity in BLEU-1

Clipping prevents repeated matching words from receiving unlimited credit. Unigram overlap ignores order, which is why a reordered candidate can still score one in this lesson.

The brevity penalty is below one only when the candidate is shorter than the reference. The explicit BLEU-1 contract avoids silently treating it as a full multi-order corpus metric.

Concept references (original code and prose):

- [Papineni et al., BLEU: a Method for Automatic Evaluation of Machine Translation](https://aclanthology.org/P02-1040/) — One-reference sentence BLEU-1 with clipping and brevity penalty; no corpus or multi-order claim.
