import random

times = int(input('enter the number: '))

i = 0

while i < times:
    print(random.randint(1,6), end=' ')
    i += 1
