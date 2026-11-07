# Differentiate an Image Smoothness Penalty

An interior pixel receives derivative contributions from several neighboring differences. Equal neighbors use the stated zero subgradient at the absolute-value kink.

This anisotropic penalty sums horizontal and vertical magnitudes separately. It differs from taking the Euclidean norm of a two-dimensional gradient vector.
