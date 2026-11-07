# Audit Multilabel Hamming Errors

Multilabel prediction makes one binary decision for every vocabulary label on every example. Hamming loss measures the fraction of those individual decisions that disagree.

A missing label and an extra label are both errors, but separate counts explain the direction of failure. The vocabulary size matters even for labels absent from both sets.
