# Decode a Combination from Its Lexicographic Rank

Ranking lets a large family of combinations be addressed without storing it. Binomial coefficients tell us exactly how many completions share each prefix.

Lexicographic order compares the first differing selected index. Choosing the next index by block sizes preserves that order and supports large ranks with exact integer arithmetic.
