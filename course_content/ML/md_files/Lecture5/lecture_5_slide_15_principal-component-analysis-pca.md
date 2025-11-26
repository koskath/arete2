# Slide 15 of Lecture 5 contains information about the Principal Component Analysis (PCA).

To decide how many principal components to retain, we look at the proportion of variance explained (PVE), which measures what percentage of the total variance is captured by a given set of PCs and can be approximated for the m-th PC as the m-th eigenvalue divided by the number of PCs; for an n*p (observations * variables) data matrix X, there can be up to min(n - 1, p) PCs, but there is no single fixed rule for selecting how many to use.
