# Learn a Count-Based Class Model

Feature counts are accumulated within each class rather than averaged per document. Additive smoothing distributes a fixed pseudo-count across the vocabulary before normalization.

Class prior counts observations, whereas feature likelihood counts tokens. Treating those as the same denominator would change the model when document lengths differ.
