# Resolve Configuration Defaults

Defaults answer an absence question. A user may intentionally disable a setting with False or specify None, and replacing those values would ignore the explicit choice.

Copying the result prevents later configuration edits from changing a defaults template reused elsewhere. This operation differs from override layers because the original config always wins.
