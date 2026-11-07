# Match Ordered IDs to Records

A lookup join must preserve the order and multiplicity of the requesting side. Sorting or deduplicating requested IDs would break alignment with the caller’s other data.

Missing-position metadata distinguishes absent records explicitly. Returning only successful matches would hide both the missing IDs and their intended positions.
