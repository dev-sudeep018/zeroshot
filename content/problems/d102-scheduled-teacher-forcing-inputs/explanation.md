# Choose Decoder Inputs with Scheduled Teacher Forcing

Scheduled teacher forcing changes which historical token the decoder receives during training. This addresses the difference between training with correct histories and generating from its own earlier predictions.

Supplied predictions are treated as fixed data here. A live autoregressive rollout would recompute later predictions after each chosen input, which is outside this deterministic batch transformation.
