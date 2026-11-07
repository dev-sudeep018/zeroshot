# Detect Mixed Primitive Column Types

A column-type audit reveals inconsistent data before model features are constructed. Numeric-looking text and actual numbers are distinct observations until a conversion policy is applied.

The report lists categories, not inferred coercions. Keeping booleans separate avoids counting a flag as a numeric measurement merely because Python permits arithmetic with it.
