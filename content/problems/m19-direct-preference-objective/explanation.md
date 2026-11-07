# Compare Preferences against a Reference Policy

When policy and reference have identical relative preferences, the margin is zero and the loss is log(2), even if both strongly favor the chosen response.

A larger positive adjusted margin reduces the loss. beta scales this margin; beta zero makes every pair have loss log(2). This operation alone does not train a language model.

Ported the upstream DPO margin to NumPy and replaced log(sigmoid(margin)) with stable logaddexp. Added explicit sequence-level inputs and original reference-shift fixtures.

Adapted code source: https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/torch_judge/tasks/dpo_loss.py
