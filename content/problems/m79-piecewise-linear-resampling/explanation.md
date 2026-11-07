# Resample between Known Measurements

Interpolation uses relative position inside a local interval, so irregular sample spacing matters. A query halfway in time receives halfway between the two neighboring values.

Endpoint extension is a separate modeling choice from interpolation. Making it explicit prevents accidental linear extrapolation beyond the measured domain.
