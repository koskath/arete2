# Slide 32 of Lecture 10 contains information about the TensorFlow’s Python API.

• At lowest level, each TensorFlow
operation is implemented using
C++ code.
• Many operations have multiple
implementations called kernels.
• Each dedicated to a specific
device (CPUs/GPUs/TPUs).
• GPUs can speed up
computations by splitting them
into many smaller chunks and
running them in parallel.
• TPUs are custom ASIC chips
built specifically for DL
operations.
