# Inspect ROUGE-L Precision and Recall

The longest common subsequence rewards preserved order without demanding contiguous matches. Inserting irrelevant candidate text leaves recall unchanged but lowers precision.

This deliberately explicit single-reference variant omits tokenization, stemming, and sentence-level aggregation. Metric names alone do not specify those evaluation choices.

Concept references (original code and prose):

- [Lin, ROUGE: A Package for Automatic Evaluation of Summaries](https://aclanthology.org/W04-1013/) — Single-reference token LCS F1; no stemming or sentence aggregation.
