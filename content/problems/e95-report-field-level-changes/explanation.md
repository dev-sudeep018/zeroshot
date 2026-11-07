# Report Field-Level Changes

A field-level diff reports enough information to inspect both additions and deletions. It preserves removed values rather than only listing names, which helps explain a change.

The comparison is shallow by field boundary but uses Python value equality for each field. It is an audit format, not a recursive patch language.
