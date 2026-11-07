# Build Next-Token Training Pairs

Shifting creates supervised targets from an existing sequence without a separate label file. The model sees a prefix position and learns to predict its immediate successor.

Masking based on explicit lengths avoids confusing a padding identifier with a genuine token that happens to use the same value. This operation prepares labels; the model must separately enforce causal attention.
