# Build an Orthonormal Basis

Each new column splits into components along existing basis vectors and an orthogonal residual. The projection coefficients form R, while normalized residuals form Q.

Modified Gram–Schmidt updates the residual after every subtraction. Its positive normalization denominator fixes the otherwise arbitrary sign of each basis column.
