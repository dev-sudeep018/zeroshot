# Trace a Class Score Back to Input Features

Input gradients measure local score sensitivity. For an affine function the gradient does not depend on the input location, although the requested class determines which weight column is relevant.

Multiplying the gradient by the input gives a zero-baseline contribution. Its row sum recovers the bias-free score; absolute gradients would lose that signed reconstruction.
