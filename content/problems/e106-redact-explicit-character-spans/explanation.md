# Redact Explicit Character Spans

Span redaction preserves alignment while hiding selected characters. Overlapping spans cover a union of positions, so repeated masking does not change the output length.

Character offsets and byte offsets differ for Unicode. This lesson uses code points, matching Python string indexing, and leaves byte accounting to a separate lesson.
