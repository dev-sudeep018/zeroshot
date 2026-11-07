# Zip Unequal Columns Explicitly

Ordinary zip stops at the shortest input and can discard data. Explicit padding retains every supplied cell when source columns have unequal lengths.

The result is rectangular, with one cell per column in each row. None is a padding marker here, so downstream code must know whether actual None values are also possible.
