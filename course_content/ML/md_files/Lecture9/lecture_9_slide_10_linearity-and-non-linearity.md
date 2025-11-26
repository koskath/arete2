# Slide 10 of Lecture 9 contains information about the Linearity and Non-Linearity.

• Linear latent-factor model with linear regression.
• Use features from latent-factor model: z =Wx
i i
• Make prediction using linear model: y =vTz
i i
• Non-linearity: Transform z by non-linear function ‘h’: z=Wx ==> y=vTh(z)
i i i i i
• Function ‘h’ transforms ‘k’ inputs to ‘k’ outputs.
• Common choice for ‘h’: Sigmoid function
• Training: Apply SGD: Compute gradient of random example ‘i’, update both ‘v’ and
‘W’.
12
CPSC 340: Machine Learning and Data Mining: http://www.stat.yale.edu/Courses/ 1997-98/101/stat101.htm
