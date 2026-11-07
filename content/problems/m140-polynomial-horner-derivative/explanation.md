# Evaluate a Polynomial and Its Slope Together

Horner evaluation avoids constructing every power separately. Differentiating each nested multiplication gives a second recurrence that computes the slope at the same time.

The update order matters because the derivative needs the previous partial polynomial. Constant and leading-zero coefficients provide simple checks on initialization.
