# Deduplicate Records by Latest Position

Update streams can contain several versions of the same entity. This policy uses stream position as recency and returns only the final version of each entity.

Dictionary overwrite alone preserves first insertion order, which is not the requested last-occurrence order. Tracking positions makes the intended ordering independent of dictionary insertion behavior.
