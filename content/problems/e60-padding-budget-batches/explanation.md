# Pack Consecutive Sequences Under a Padding Budget

Dense padded computation often scales with batch_size times max_length, not the sum of true sequence lengths. The batch planner must account for this shared padding cost.

This lesson uses an order-preserving greedy policy rather than sorting or optimizing globally. Keeping original order makes the output predictable and preserves a caller-defined sequence schedule.
