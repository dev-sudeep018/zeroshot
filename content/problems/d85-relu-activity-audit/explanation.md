# Find Inactive ReLU Neurons

A batch-inactive ReLU emits zero for every observed example. Under the usual derivative convention, these examples also send zero gradient through that unit.

Mean output and activity fraction describe different behaviors. A rarely active neuron can produce large values, so inspecting both helps distinguish frequency from magnitude.
