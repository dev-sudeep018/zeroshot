# Compare Two Inventories

A snapshot comparison needs to distinguish structural changes from changed values. An item newly present with zero stock is added even though it contributes no units.

Sorting the output makes reports deterministic across dictionary insertion orders. The changed rows retain both values so a reviewer can reconstruct the quantity difference.
