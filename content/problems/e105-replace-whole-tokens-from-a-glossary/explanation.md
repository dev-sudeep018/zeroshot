# Replace Whole Tokens from a Glossary

A glossary expands known tokens while leaving unknown tokens intact. The matching unit is a complete whitespace-delimited token, which makes the transformation predictable.

Joining creates a canonical separator between token slots. An empty replacement is still a slot, so deleting a token entirely would be a different operation.
