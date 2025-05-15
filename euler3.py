from ourlib import *

num = 600851475143
num = 36
primes = []
check = 1

for i in range(2, 10000):
    if is_prime(i):
        primes.append(i)

for x in primes:
    if num % x == 0:
        print(x)
        check *= x 

print(num - check)