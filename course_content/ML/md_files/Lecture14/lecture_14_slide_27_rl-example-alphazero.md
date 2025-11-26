# Slide 27 of Lecture 14 contains information about the RL Example: AlphaZero.

• [2017] AlphaZero is a single system that taught itself from scratch how to master
games of chess, shogi (Japanese chess).
• How it works?
• To learn each game, an untrained NN plays millions of games against itself via a
process of trial and error.
• At first, it plays completely randomly, but over time system learns from wins,
losses, and draws to adjust the parameters of NN, making it more likely to choose
advantageous moves in future.
• The amount of training NN needs depends on complexity of game, taking
approximately
• 9 hours for chess
• 12 hours for shogi
• 13 days for Go.
