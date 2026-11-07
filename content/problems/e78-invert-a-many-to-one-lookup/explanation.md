# Invert a Many-to-One Lookup

Inverting a lookup changes the direction of access. A many-to-one forward mapping becomes one-to-many in reverse, so overwriting would discard valid source keys.

Retaining insertion order allows the reverse groups to reflect the source catalog order. The function deliberately does not require target values to be unique.
