# Measure Four-Connected Grid Regions

Flood fill explores the full region reachable through edge-sharing moves. Marking a cell when it is scheduled prevents two neighboring cells from adding it twice.

Perimeter counts local exposed edges, so both outside borders and enclosed holes contribute. Summing component sizes recovers the total number of true cells, while diagonal contacts leave separate labels.
