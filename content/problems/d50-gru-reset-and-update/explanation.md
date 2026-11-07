# Distinguish GRU Reset from Update Gates

Closing reset prevents the recurrent contribution from shaping the candidate. Update can still retain old state directly.

Supplying affine contributions makes gate placement inspectable. This is not a learned GRU layer or a reset-before-matrix convention.
