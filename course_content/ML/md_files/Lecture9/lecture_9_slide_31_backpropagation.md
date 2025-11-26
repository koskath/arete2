# Slide 31 of Lecture 9 contains information about the Backpropagation.

• Cost of backpropagation:
• Forward pass dominated by matrix multiplications by W(1), W(2), W(3), and ‘v’.
• If you have ‘m’ layers and all z have ‘k’ elements, cost would be O(dk + mk2).
i
• Backward pass has same cost as forward pass.
• For multi-class or multi-label classification, you replace ‘v’ by a matrix.
34
CPSC 340: Machine Learning and Data Mining: http://www.stat.yale.edu/Courses/ 1997-98/101/stat101.htm
