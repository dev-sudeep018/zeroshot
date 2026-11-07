# Update Momentum from a Lookahead Gradient

Momentum carries previous movement forward, while the lookahead gradient corrects the anticipated position. Naming the velocity convention prevents confusion with libraries that store an unscaled gradient buffer.

When momentum is zero the update reduces to SGD. When learning rate is zero, a nonzero previous velocity still moves the parameters under this recurrence.
