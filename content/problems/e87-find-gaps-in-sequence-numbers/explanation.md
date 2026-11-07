# Find Gaps in Sequence Numbers

Sequence audits need explicit expected boundaries. Inferring the range from observed IDs would miss gaps before the first observed item or after the last.

Duplicates do not fill additional sequence positions. A set removes repeated observations, while an ascending range provides deterministic missing-ID order.
