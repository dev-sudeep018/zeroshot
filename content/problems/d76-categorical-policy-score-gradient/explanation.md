# Differentiate a Categorical Policy Objective

A positive advantage makes gradient descent increase the chosen action logit relative to the others. A negative advantage reverses that direction.

This explicit derivative is a small score-function calculation from supplied samples. Estimating useful advantages and collecting rollouts are separate parts of policy optimization.

Conceptual reading: https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html
