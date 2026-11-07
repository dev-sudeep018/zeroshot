# Turn Fixed Uniform Draws into Categories

Inverse-CDF sampling maps uniform draws into categories with prescribed probabilities. Supplying the draws makes the transformation deterministic and testable.

Strictly greater cumulative mass determines boundary behavior. A left-sided search can select a zero-probability category at a repeated cumulative boundary, so the convention matters.
