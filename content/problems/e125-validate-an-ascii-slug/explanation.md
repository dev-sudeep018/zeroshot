# Validate an ASCII Slug

Resource slugs provide a predictable identifier from a display name. Collapsing separators prevents cosmetic differences in punctuation from generating awkward runs of hyphens.

ASCII-only input avoids silently transliterating names with an unspecified policy. Slugs are not guaranteed unique, so a real registry must handle collisions separately.
