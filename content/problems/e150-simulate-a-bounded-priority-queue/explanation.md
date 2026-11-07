# Simulate a Bounded Priority Queue

Priority queues let urgent tasks overtake lower-priority tasks while retaining a stable order among equals. Bounded capacity makes overload behavior explicit.

This policy rejects new work when full, even if the new job has a higher priority. Evicting existing work would require a different contract and accounting model.
