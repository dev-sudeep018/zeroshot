# Engineering expansion to the 450-lesson curriculum

This batch adds 100 distinct runnable lessons, e63–e162: 80 beginner and 20 intermediate. Each has a documented input/output contract, three worked examples, two hints, an explanation, a starter, a reference implementation, and executable public tests. All 1010 public cases pass natively, all 300 displayed examples match execution, and every starter fails its checks before implementation.

Beginner lessons work with realistic records, inventory requests, grouping, ordering, text offsets, parsing, missing data, category encoding, and retrieval measurements. They require reasoning about data and edge cases rather than printing output or recalling syntax. Intermediate lessons add replay protection, time windows, queues, dependency graphs, byte framing, and incremental rebuilding.

## Provenance

All exercise prose, code, examples, and test fixtures in this batch are original ZeroShot work. No external platform lesson or implementation was copied. Standard Python facilities such as CSV, JSON, UTF-8, and SHA-256 implement the explicitly documented contracts; these are not claims of imported educational content.

## Validation

`python -m unittest discover -s tests/python -p test_engineering450.py -v` passes 23 tests. In addition to executing every package, independent checks cover stock conservation, complete pagination, FIFO transitions, stable sorting, UTF-8 offsets, CSV/query round trips, training-only vocabulary fitting, exhaustive multilabel comparisons, hash split boundaries, time-window partitions, dependency ordering against all small graph permutations, message budgets, symmetric byte-frame limits, and contiguous checkpoints.

The byte framing exercise enforces a 10,000,000-byte complete-stream limit in both directions, including headers. A boundary regression round-trips a stream exactly at that limit and rejects the next byte. Hash holdout public examples exercise actual mixed bucket membership and strict threshold equality, not only all-train or all-holdout settings.

Browser/Pyodide execution and whole-application CI are integration gates handled by the parent curriculum release; native validation alone does not claim those checks passed.

| ID   | Lesson                                       | Difficulty   | Public cases |
| ---- | -------------------------------------------- | ------------ | -----------: |
| e63  | Normalize and Deduplicate Tags               | beginner     |           10 |
| e64  | Route Support Tickets                        | beginner     |           10 |
| e65  | Reconcile Stock Requests                     | beginner     |           10 |
| e66  | Summarize Completed Orders                   | beginner     |           10 |
| e67  | Apply Sequential Balance Changes             | beginner     |           10 |
| e68  | Find the First Matching Record               | beginner     |           10 |
| e69  | Extract Optional Record Fields               | beginner     |           10 |
| e70  | Project Records to a Schema                  | beginner     |           10 |
| e71  | Rename Record Fields Safely                  | beginner     |           10 |
| e72  | Index Unique Records                         | beginner     |           10 |
| e73  | Group Records by Category                    | beginner     |           10 |
| e74  | Deduplicate Records by Latest Position       | beginner     |           10 |
| e75  | Compare Two Inventories                      | beginner     |           10 |
| e76  | Merge Configuration Layers                   | beginner     |           10 |
| e77  | Resolve Configuration Defaults               | beginner     |           10 |
| e78  | Invert a Many-to-One Lookup                  | beginner     |           10 |
| e79  | Allocate Round-Robin Work                    | beginner     |           10 |
| e80  | Split Work into Fixed Batches                | beginner     |           10 |
| e81  | Paginate Records with Metadata               | beginner     |           10 |
| e82  | Interleave Unequal Streams                   | beginner     |           10 |
| e83  | Flatten One Level of Records                 | beginner     |           10 |
| e84  | Expand Repeated Job Requests                 | beginner     |           10 |
| e85  | Count Adjacent Status Transitions            | beginner     |           10 |
| e86  | Summarize Streak Lengths by Status           | beginner     |           10 |
| e87  | Find Gaps in Sequence Numbers                | beginner     |           10 |
| e88  | Audit Duplicate Identifiers                  | beginner     |           10 |
| e89  | Match Ordered IDs to Records                 | beginner     |           10 |
| e90  | Zip Unequal Columns Explicitly               | beginner     |           10 |
| e91  | Unzip Record Columns                         | beginner     |           10 |
| e92  | Build a Multi-Key Stable Sort                | beginner     |           10 |
| e93  | Select the Best Record Per Group             | beginner     |           10 |
| e94  | Filter Records by Inclusive Ranges           | beginner     |           10 |
| e95  | Report Field-Level Changes                   | beginner     |           10 |
| e96  | Apply Explicit Record Patches                | beginner     |           10 |
| e97  | Build a Quantity Histogram                   | beginner     |           10 |
| e98  | Validate a Required-Field Schema             | beginner     |           10 |
| e99  | Validate Foreign-Key References              | beginner     |           10 |
| e100 | Reconcile Ordered Membership Lists           | beginner     |           10 |
| e101 | Merge Sorted Event Streams                   | beginner     |           10 |
| e102 | Track Open and Closed Tasks                  | beginner     |           10 |
| e103 | Normalize Whitespace in Text                 | beginner     |           10 |
| e104 | Tokenize ASCII Words with Offsets            | beginner     |           10 |
| e105 | Replace Whole Tokens from a Glossary         | beginner     |           10 |
| e106 | Redact Explicit Character Spans              | beginner     |           10 |
| e107 | Extract Bounded Context Windows              | beginner     |           10 |
| e108 | Match Case-Insensitive Exact Answers         | beginner     |           10 |
| e109 | Count Unique Terms Per Document              | beginner     |           10 |
| e110 | Filter Stopwords Without Reordering          | beginner     |           10 |
| e111 | Build UTF-8 Character Offset Maps            | beginner     |           10 |
| e112 | Encode Tokens with an Unknown ID             | beginner     |           10 |
| e113 | Decode Token IDs with Explicit Fallback      | beginner     |           10 |
| e114 | Measure Truncation of Token Sequences        | beginner     |           10 |
| e115 | Validate BIO Entity Tag Transitions          | beginner     |           10 |
| e116 | Read Simple Key-Value Lines                  | beginner     |           10 |
| e117 | Parse Strict Boolean Settings                | beginner     |           10 |
| e118 | Parse Bounded Decimal Integers               | beginner     |           11 |
| e119 | Parse Durations with Explicit Units          | beginner     |           10 |
| e120 | Parse Semantic Version Triples               | beginner     |           10 |
| e121 | Parse CSV Records by Header                  | beginner     |           11 |
| e122 | Serialize CSV Records in Schema Order        | beginner     |           11 |
| e123 | Parse JSON Lines with Error Positions        | beginner     |           10 |
| e124 | Canonicalize JSON for Cache Keys             | beginner     |           10 |
| e125 | Validate an ASCII Slug                       | beginner     |           10 |
| e126 | Normalize Relative Resource Paths            | beginner     |           11 |
| e127 | Parse URL Query Pairs                        | beginner     |           11 |
| e128 | Encode Query Parameters Deterministically    | beginner     |           10 |
| e129 | Audit Tabular Row Widths                     | beginner     |           10 |
| e130 | Detect Mixed Primitive Column Types          | beginner     |           10 |
| e131 | Find Blank and Missing Cells                 | beginner     |           10 |
| e132 | Check Monotonic Event Times                  | beginner     |           10 |
| e133 | Validate Unique Composite Keys               | beginner     |           10 |
| e134 | Forward-Fill Missing Values with a Limit     | beginner     |           10 |
| e135 | Check Allowed Category Values                | beginner     |           10 |
| e136 | Apply Training Category Maps                 | beginner     |           10 |
| e137 | Summarize Rule-Based Data Quality            | beginner     |           10 |
| e138 | Audit Multilabel Hamming Errors              | beginner     |           11 |
| e139 | Score Exact-Match Predictions by Group       | beginner     |           10 |
| e140 | Compute Retrieval Precision at a Cutoff      | beginner     |           10 |
| e141 | Measure Ranking Coverage Across Queries      | beginner     |           10 |
| e142 | Find Pairwise Result-Set Disagreements       | beginner     |           10 |
| e143 | Build Deterministic Holdout by ID Hash       | intermediate |           13 |
| e144 | Assign Events to Fixed Time Windows          | intermediate |           10 |
| e145 | Sessionize Events by Inactivity              | intermediate |           10 |
| e146 | Deduplicate Idempotency Keys                 | intermediate |           10 |
| e147 | Schedule Bounded Retries                     | intermediate |           10 |
| e148 | Trace a Circuit Breaker                      | intermediate |           10 |
| e149 | Simulate a FIFO Work Queue                   | intermediate |           10 |
| e150 | Simulate a Bounded Priority Queue            | intermediate |           10 |
| e151 | Compute Worker Makespan                      | intermediate |           10 |
| e152 | Select Jobs by Dependencies                  | intermediate |           10 |
| e153 | Find Transitive Dependency Impact            | intermediate |           10 |
| e154 | Build a Prefix Search Index                  | intermediate |           10 |
| e155 | Match Multiword Phrases Exactly              | intermediate |           10 |
| e156 | Segment Sentences with a Small State Machine | intermediate |           10 |
| e157 | Budget Messages by UTF-8 Bytes               | intermediate |           10 |
| e158 | Build Reversible Length-Prefixed Frames      | intermediate |           11 |
| e159 | Verify Payload Digests                       | intermediate |           10 |
| e160 | Apply a Versioned Cache Policy               | intermediate |           10 |
| e161 | Reconcile Append-Only Checkpoints            | intermediate |           10 |
| e162 | Plan a Minimal Incremental Rebuild           | intermediate |           10 |
