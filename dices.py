import random

outcome = [0,0,0,0,0,0,0,0,0,0,0]

for i in range(200):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    result = dice1 + dice2
    outcome[result - 2] += 1

print(outcome)