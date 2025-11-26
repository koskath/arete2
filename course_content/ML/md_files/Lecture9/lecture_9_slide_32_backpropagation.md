# Slide 32 of Lecture 9 contains information about the Backpropagation.

(Computing gradients)
• An efficient technique for computing gradients automatically.
• Backpropagation training algorithm* to train MLPs.
1. For each training instance: backpropagation algorithm first makes a prediction (forward
pass) and measures error.
2. Then goes through each layer in reverse to measure error contribution from each
connection (backward pass).
3. Finally tweaks connection weights to reduce error (Gradient Descent step).
35
*David Rumelhart et al. “Learning Internal Representations by Error Propagation,” (Defense Technical Information Center technical report, September
1985).
