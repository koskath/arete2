# Slide 18 of Lecture 12 contains information about the Learning Rate: Setting the Step-Size.

• Stochastic gradient is very sensitive to step size in deep models.
• A common approach:
• Run SG for a while with a fixed step-size.
• Occasionally measure error and plot progress.
• If error is not decreasing, decrease step-size.
• Bias step-size multiplier: use bigger step-size for bias variables.
• Momentum: Add term that moves in previous direction where βt=0.9
