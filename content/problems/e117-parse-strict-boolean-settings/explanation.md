# Parse Strict Boolean Settings

Configuration values often arrive as text. Treating any nonempty string as true turns the literal false into a dangerous configuration error.

A small accepted vocabulary makes this conversion auditable. Unknown values are rejected rather than guessed, which helps callers catch misspellings early.
