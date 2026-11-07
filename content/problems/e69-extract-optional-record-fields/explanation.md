# Extract Optional Record Fields

Optional fields need a deliberate absence policy. Treating zero or False as missing would change valid measurements or settings during extraction.

Returning copied values protects the source records from later edits to extracted containers. The list keeps row alignment so it can be paired with other extracted columns.
