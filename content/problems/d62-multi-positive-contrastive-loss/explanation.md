# Average Log Probabilities across Positive Partners

An anchor with several positives contributes the mean of their individual log losses. Taking the log of summed positive probability implements a different objective.

Supplied similarity scores isolate the objective from embedding normalization and temperature choices. Labels determine partner membership rather than a single diagonal match.
