# Reconstruct Logical Tokens from KV Pages

Paging allows a sequence to occupy noncontiguous physical blocks. A logical page table provides the ordering needed to reconstruct token history.

This model demonstrates address translation and tail truncation. It does not claim a GPU memory allocator, attention kernel, or measured serving-speed improvement.

Concept references (original code and prose):

- [Kwon et al., Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) — Logical page-table gathering only; no GPU kernel, memory allocator, or throughput claim.
