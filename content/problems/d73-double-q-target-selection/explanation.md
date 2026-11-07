# Separate Action Selection from Action Evaluation

If the estimators disagree about the best action, Double Q uses the target value at the online-selected action, even when that is not the target maximum.

This exercise computes the target from supplied estimates. Network updates, replay, and target-network synchronization belong to the surrounding training system.

Conceptual reading: https://arxiv.org/abs/1509.06461
