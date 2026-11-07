# Verify Payload Digests

Content digests detect changed payload bytes during storage or transfer. A batch report should identify the exact records that need repair.

A plain hash checks consistency against the supplied digest; it does not authenticate an untrusted sender. Malformed digest text is a contract error rather than evidence of changed content.
