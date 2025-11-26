# Slide 14 of Lecture 5 contains information about the Principal Components (PCs).

• Overall PC calculation process:
• For each PC:
• PCA finds a zero-centered unit vector pointing in the direction of PC.
• Direction of unit vectors returned by PCA is not stable*.
• If you perturb training set slightly and run PCA again
• Unit vectors may point in opposite direction as original vectors.
• Still, they will lie on same axes.
*Sincetwoopposing unitvectors lieonthe same axis.
