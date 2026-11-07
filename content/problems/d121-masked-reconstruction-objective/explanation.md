# Restrict Reconstruction Loss to Masked Patches

Masking the objective changes both which residuals contribute and the normalization denominator. A batch with fewer selected patches should not reduce loss merely because more visible patches are ignored.

The gradient is twice the residual divided by the number of scored scalar features. Keeping zero gradients on unselected positions makes the restricted objective explicit.
