# Control a Linear Layer’s Maximum Gain

Spectral normalization controls the worst-case Euclidean gain of a linear layer. It differs from normalizing each column or using the Frobenius norm, which can produce a different scale.

The bound concerns this linear map. Nonlinearities and compositions require separate reasoning; setting one layer’s gain does not alone guarantee a whole model’s robustness.
