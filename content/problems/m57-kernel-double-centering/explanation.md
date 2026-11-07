# Center Features through Their Kernel

If K=X X.T, centering the feature rows first gives (X-mean(X))(X-mean(X)).T. Expanding that product yields the two mean subtractions and one grand-mean addition.

A centered training Gram matrix has row and column sums near zero. Adding a constant to every original kernel entry disappears under the transformation.
