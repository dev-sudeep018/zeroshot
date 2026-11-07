# Select the Best Record Per Group

Grouped selection preserves the best full record instead of merely computing a maximum number. This retains metadata needed to explain or act on the selected result.

Initializing from the first group member handles negative scores correctly. A default score of zero would mistakenly reject every negative candidate.
