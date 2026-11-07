# Verify Draft Tokens and Correct a Rejection

Acceptance reweights draft proposals toward the target distribution. On rejection, the residual distribution supplies probability mass the draft underrepresented.

The caller supplies probabilities conditioned on the appropriate prefix and reproducible uniform draws. This lesson isolates verification and leaves model execution, replacement sampling, and bonus-token generation outside the contract.

Concept references (original code and prose):

- [Leviathan et al., Fast Inference from Transformers via Speculative Decoding](https://proceedings.mlr.press/v202/leviathan23a.html) — Supplied draft-prefix verification and normalized residual distribution; no bonus-token generation or model serving.
