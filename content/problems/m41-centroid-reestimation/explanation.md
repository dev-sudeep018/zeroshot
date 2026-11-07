# Move Cluster Centers to Their Assigned Means

For fixed membership, differentiating the sum of squared distances with respect to a center gives the group mean. This is the update step of Lloyd-style k-means.

An empty group has no mean. Keeping its previous center makes the behavior explicit without silently changing the number or identity of clusters.
