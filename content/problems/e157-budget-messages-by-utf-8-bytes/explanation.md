# Budget Messages by UTF-8 Bytes

Payload budgets often count bytes on the wire rather than visible characters. UTF-8 characters can occupy different numbers of bytes, making character counts unreliable.

Keeping a prefix preserves chronological message order. A later short message cannot bypass an earlier message that does not fit under this policy.
