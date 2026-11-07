# Trace Precision and Recall at Tied Scores

The curve is a sequence of achievable decision rules. Moving tied observations one at a time would invent operating points that no threshold can reproduce.

This lesson reports observed points without integrating an area. Average precision and trapezoidal PR area make different aggregation choices and should not be silently substituted.

Concept references (original code and prose):

- [scikit-learn precision-recall curve documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html) — Only observed descending-score thresholds; no synthetic endpoint or area aggregation.
