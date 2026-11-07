# Sum the Probability of CTC Alignments

Consecutive repeated frame labels merge before blanks are removed. Thus a target with two identical labels needs a blank frame between their emissions.

The forward dynamic program sums paths rather than selecting the most probable path. Greedy frame decoding does not compute a target likelihood.
