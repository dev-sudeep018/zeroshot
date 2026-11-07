# Find the First Matching Record

Searching by a small query dictionary separates record order from matching criteria. Every requested field must agree, while additional record fields are allowed.

Using row.get(key) alone confuses a missing field with an explicitly stored None. Checking membership first retains that distinction and makes empty-query behavior well defined.
