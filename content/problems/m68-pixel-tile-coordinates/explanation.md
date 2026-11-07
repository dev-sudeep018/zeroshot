# Locate Pixels inside Image Tiles

Flat indexing and tiling are different coordinate transforms. A flat index counts across full image rows, while tile coordinates count blocks and local coordinates count positions within a block.

The identity row=tile_row\*tile_height+local_row, with the analogous column identity, reconstructs every pixel. It still holds when the final tiles are smaller than the requested tile size.
