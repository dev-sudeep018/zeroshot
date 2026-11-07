# Explore Beam Search on a Transition Table

Beam search trades memory and compute for a larger candidate frontier. A wider beam can retain an initially weaker branch that later becomes the best surviving sequence.

This explicit scoring variant has no length normalization, repetition penalty, or stochastic sampling. A completed short sequence can therefore outrank a longer sequence whose extra log scores reduce its total.
