# Filter Records by Inclusive Ranges

Range rules form a conjunction: a record is retained only if every configured field is valid and within bounds. Checking only one field would allow partially invalid rows through.

Validation is independent of filtering. A missing or nonnumeric field is a malformed input, even if another condition would already exclude that row.
