# Match Multiword Phrases Exactly

Exact phrase matching is useful for dictionary-based tagging and transparent retrieval filters. Keeping tokens separate avoids accidental substring matches inside words.

Overlapping matches are valid occurrences. Jumping ahead by the phrase length after a match would miss repeated-token patterns.
