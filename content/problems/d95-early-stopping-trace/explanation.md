# Stop Training after Sustained Validation Stalls

Patience tolerates isolated non-improving epochs while limiting repeated wasted evaluation. Remembering a meaningful best value lets several small improvements eventually exceed min_delta.

Stopping logic is a policy, so boundary conventions must be explicit. It uses validation observations and does not restore model parameters; the returned best epoch identifies which checkpoint a training loop should restore.
