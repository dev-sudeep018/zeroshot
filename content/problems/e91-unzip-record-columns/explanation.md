# Unzip Record Columns

Column extraction changes storage layout while preserving row alignment. Keeping every column in the same row order is essential for later model features and targets.

This strict schema differs from projection with missing-value filling. It catches incomplete records before they enter a rectangular dataset.
