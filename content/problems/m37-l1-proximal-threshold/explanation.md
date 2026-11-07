# Create Sparsity with a Proximal Step

For a scalar input x, minimizing one half of (z-x)^2 plus threshold\*abs(z) gives a signed shrinkage rule. The penalty wins completely when the input magnitude is below the threshold.

Hard thresholding would leave retained values untouched. Soft thresholding also moves every retained coefficient toward zero, which matters when combining this operator with gradient steps.
