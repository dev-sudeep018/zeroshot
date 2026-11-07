# Move a Target Network Gradually

A partial copy reduces abrupt movement of the target used for bootstrapping. It is an exponential moving average when applied repeatedly to successive online parameters.

The rate convention must be explicit: using a retention coefficient as an online rate reverses the behavior. This operation synchronizes parameters and does not compute gradients.

Conceptual reading: https://spinningup.openai.com/en/latest/algorithms/ddpg.html
