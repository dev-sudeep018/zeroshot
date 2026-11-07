# Parse Bounded Decimal Integers

Strict integer parsing protects data contracts from extra syntax accepted by general-purpose parsers. Decimal strings, floats, and scientific notation are different formats.

Leading zeros do not change the value. Removing redundant zeros before conversion keeps an otherwise valid long zero prefix from depending on interpreter integer-string limits.
