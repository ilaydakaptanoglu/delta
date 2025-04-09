#while loop

'''
import mylib, random

times = 10
i = 0
while i < times:
    print(random.randint(1,6), end=' ')
    i += 1
'''

import ourlib, random

times = int(input("Enter the number: "))
i = 0
while i < times:
    print(random.randint(1,6), end=' ')
    i += 1
