# Parse Durations with Explicit Units

Duration fields combine a quantity with a unit. Converting into one integer base unit avoids confusion when milliseconds, seconds, and minutes appear together.

The output bound applies after conversion. A small-looking number of minutes can exceed the allowed millisecond range, so checking only the raw number is insufficient.
