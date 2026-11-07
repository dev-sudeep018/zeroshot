# Separate LSTM Cell Memory from Hidden Output

A closed output gate can conceal information that remains in the cell. Treating hidden output as the next cell loses this distinction.

This exercise isolates memory arithmetic. A complete LSTM also computes the supplied preactivations from an input and previous hidden state.
