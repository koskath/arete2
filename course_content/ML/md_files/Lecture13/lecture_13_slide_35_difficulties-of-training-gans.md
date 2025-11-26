# Slide 35 of Lecture 13 contains information about the Difficulties of Training GANs.

1.
Generator and discriminator constantly try to outsmart each other lead to
no player would be better off changing their own strategy, assuming other
players do not change theirs.
2.
Generator produces perfectly realistic images and discriminator is forced to
guess (50% real, 50% fake) (Not guaranteed).
3.
Generator’s outputs gradually become less diverse (called mode collapse).
4.
Generator and discriminator are constantly pushing against each other,
parameters may end up oscillating and becoming unstable.
