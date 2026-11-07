# Separate Codebook and Commitment Gradients

The codebook learns to approach encoder outputs while the commitment term discourages encoder drift from selected codes. Stop-gradient makes these objectives asymmetric in their parameters.

Here codes are matched vectors, not a full table. A later lookup-backward operation would accumulate these code gradients when several examples share a code index.
