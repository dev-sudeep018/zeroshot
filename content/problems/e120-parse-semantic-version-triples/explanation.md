# Parse Semantic Version Triples

Version ordering is hierarchical. A larger major version wins even if every later component is smaller, and numeric comparison avoids treating 10 as less than 2.

This exercise implements a restricted triple format, not the complete semantic-version specification. Rejecting unsupported suffixes keeps that distinction explicit.
