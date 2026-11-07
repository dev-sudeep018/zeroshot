# Rename Record Fields Safely

Schema migrations often rename fields while retaining values. Applying all renames from the original keys avoids one rename accidentally changing the input to another.

A collision would destroy a value through overwriting. Rejecting it makes the migration explicit, while ignoring absent source keys allows one rename policy to serve heterogeneous records.
