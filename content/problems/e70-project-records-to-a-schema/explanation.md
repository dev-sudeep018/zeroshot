# Project Records to a Schema

Projection makes heterogeneous records conform to a chosen output schema. It controls which fields leave the pipeline and supplies a consistent representation for absent values.

The schema order is explicit rather than inherited from arbitrary source dictionaries. This helps later CSV or column-oriented exports agree on field order.
