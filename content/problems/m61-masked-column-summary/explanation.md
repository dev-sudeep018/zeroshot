# Summarize Only Observed Cells

Missingness is a property of the mask, not of a particular numeric value. An observed zero contributes to the denominator, while an unobserved large value contributes to neither sum nor count.

Returning counts alongside means makes coverage visible. The fallback prevents division by zero but does not pretend that an unobserved column has supporting data.
