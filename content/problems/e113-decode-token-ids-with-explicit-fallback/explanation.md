# Decode Token IDs with Explicit Fallback

Decoding restores readable tokens from integer features. Unique vocabulary IDs are necessary because two different tokens cannot both be the unambiguous inverse of one number.

A fallback makes decoding total over valid nonnegative IDs, while the unknown-ID report keeps that lossy behavior visible.
