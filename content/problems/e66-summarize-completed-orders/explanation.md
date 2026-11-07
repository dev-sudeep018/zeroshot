# Summarize Completed Orders

Grouped aggregation combines several rows into one summary per customer. Filtering first prevents cancelled orders from influencing totals or creating empty customer groups.

Integer cents avoid binary floating-point rounding for this simplified currency representation. The lesson does not perform tax or exchange-rate calculations; it preserves exact integer addition.
