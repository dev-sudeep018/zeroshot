# Interpret the Top Two Class Scores

The top-two margin isolates how strongly the winning score separates from its closest competitor. Exact ties have zero margin with deterministic label selection.

Margins are not calibrated probabilities. Rescaling logits changes their margin even when class ordering is unchanged, so the score scale matters when comparing models.
