# Summarize Rule-Based Data Quality

A small rule engine separates the data being audited from the audit policy. Named rules make reports understandable when several checks target the same field.

Rule failure is different from an invalid rule definition. The former belongs in a per-row report, while malformed definitions should stop the audit with an error.
