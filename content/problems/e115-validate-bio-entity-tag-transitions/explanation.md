# Validate BIO Entity Tag Transitions

BIO tags distinguish the beginning and interior of named entity spans. Auditing transitions catches an interior tag that has no compatible predecessor.

This task reports raw local inconsistencies rather than repairing the sequence. An invalid tag still exists in the raw trace and can be a compatible predecessor for the next tag.
