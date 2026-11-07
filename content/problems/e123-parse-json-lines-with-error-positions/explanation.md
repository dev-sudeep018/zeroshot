# Parse JSON Lines with Error Positions

JSON Lines lets pipelines process records independently. Keeping a rejection list makes partial ingestion explicit and preserves the source locations needed for repair.

Rejecting duplicate keys and nonfinite numbers removes ambiguities that some parsers otherwise accept. A valid JSON value can still fail this application contract when it is not an object.
