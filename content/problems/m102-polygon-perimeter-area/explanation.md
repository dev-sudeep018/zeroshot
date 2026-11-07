# Walk a Closed Polygon

The closing edge is easy to omit when vertices are stored without repeating the start. Treating the sequence cyclically ensures both perimeter and area include that edge.

Perimeter is unchanged when traversal direction reverses, but signed shoelace area changes sign. For a simple polygon its absolute value is geometric area; self-crossing paths need a different interpretation.
