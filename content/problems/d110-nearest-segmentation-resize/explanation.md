# Resize Class Labels without Inventing Classes

Nearest-neighbor selection preserves the set of available class labels. It is appropriate when numeric distances between label IDs have no meaning.

Different nearest-neighbor coordinate conventions can disagree at boundaries. Naming this floor mapping makes the operation reproducible and prevents accidental comparison with a different library convention.
