# Keep Related Rows in One Split

Group-aware evaluation prevents identity or session information from appearing in both splits. The chosen holdout groups define the experimental unit, even when groups have unequal sizes.

The function only materializes a specified partition; it does not optimize group balance or choose holdout groups. Returning row indices makes the split reusable across aligned arrays.
