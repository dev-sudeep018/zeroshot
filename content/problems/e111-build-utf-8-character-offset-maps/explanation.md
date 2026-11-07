# Build UTF-8 Character Offset Maps

A tokenizer may report character spans while a storage format uses byte positions. A boundary map translates between these coordinate systems without decoding arbitrary partial bytes.

Code points are not grapheme clusters: a letter plus a combining mark has two boundaries here. UTF-8 characters occupy between one and four bytes, so multiplying by a fixed width is incorrect.
