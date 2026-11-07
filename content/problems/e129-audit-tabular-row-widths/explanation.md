# Audit Tabular Row Widths

Ragged rows can misalign features and targets when imported into a table. Reporting both row position and observed width makes the mismatch actionable.

The expected width comes from the schema, not the first row. Otherwise a malformed first row could redefine what every later row is judged against.
