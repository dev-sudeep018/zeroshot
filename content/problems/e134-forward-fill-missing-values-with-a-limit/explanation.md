# Forward-Fill Missing Values with a Limit

Forward filling uses only earlier observations, which avoids leaking future information into a time-ordered dataset. A limit prevents stale measurements from propagating indefinitely.

Only None is missing in this exercise. Zero and False are observations and must become eligible fill values rather than being skipped.
