# Apply Explicit Record Patches

An explicit patch language separates operations from data values. That allows None to be stored as a legitimate value while deletion remains unambiguous.

Operation order matters: setting a key can make a later deletion valid, and deleting then setting recreates it. Rejecting absent deletions helps catch stale or incorrect patches.
