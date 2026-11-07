# Recover a Triangle from Side Lengths

Side lengths determine a triangle up to rigid motion and reflection when the strict triangle inequalities hold. The cosine rule recovers its angles without requiring coordinates.

Clipping the computed cosine protects arccos from tiny roundoff beyond its domain. It does not make impossible side lengths valid, so triangle validation must occur first.
