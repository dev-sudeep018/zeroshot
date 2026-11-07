# Trace Returns across Episode Boundaries

The backward recurrence is equivalent to a discounted sum of future rewards up to a terminal boundary, plus a discounted bootstrap if the rollout ends first.

Rewards from a later episode cannot cross a terminal transition. A collected rollout ending is not itself proof that the environment terminated.

Conceptual reading: https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html
