# Validate Foreign-Key References

Foreign-key validation checks whether a relation points to an existing entity. It catches disconnected records before a join silently drops them.

Parent uniqueness ensures each foreign key has at most one target. Child references may repeat, and every offending child row receives its own audit position.
