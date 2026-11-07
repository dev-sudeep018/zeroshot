# Count Parameters across a Dense Network

Each dense output neuron connects to every input coordinate. Counting adjacent pairs exposes why changing one hidden width affects two parameter blocks.

Parameter storage differs from activation storage and dataset size. Bias flags change the trainable count without changing the number of output neurons.
