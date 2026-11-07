# Recover the Best Label Sequence with Backtracking

A temporarily worse prefix may become the best complete sequence through a favorable transition. Keeping one state for each ending label preserves those possibilities.

This reference stores short prefix tuples for explicit deterministic ties. A production decoder can store backpointers, provided it preserves the documented tie policy.
