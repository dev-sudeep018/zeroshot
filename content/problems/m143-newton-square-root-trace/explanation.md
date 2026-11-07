# Trace Newton Updates toward a Square Root

Newton updates use a local linear approximation of x squared minus the target. The simplified recurrence avoids explicitly calculating the derivative each time.

A positive initial guess keeps every estimate positive. For a zero target the estimate halves each time, which makes a useful exact trace check.
