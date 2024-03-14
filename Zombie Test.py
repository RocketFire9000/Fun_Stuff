"""
Rules:
10 by 10 grid
1 zombie in the back row in a random spot
User gets to place their character anywhere except the back row
Zombie has 40% change to bite forward, 40% chance to bite in the direction of their dominant hand, 20% chance to bite in direction of non-dominant hand
Zombies cannot bite behind, and cannot bite other zombies. They also cannot bite diagonal. If stuck in a corner, they will always bite forwards.
"""
from random import randint
i = 1
print(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
while i < 9:
    print(i, "| " * 10)
    i += 1
if i == 9:
    print("10" + "| " * 10)
