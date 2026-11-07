# Parse CSV Records by Header

CSV is a structured format with quoting rules, not simply text split on commas. A quoted field can include both commas and newlines without creating extra records.

A unique header and fixed row width make conversion to dictionaries lossless. Cells stay strings so numeric interpretation can follow an explicit schema later.
