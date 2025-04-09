from ourlib import *

stop = 4000000
fibo_nums = []

i = 1
while fibo(i) < stop:
    num = fibo(i)
    if num % 2 == 0:
        fibo_nums.append(num)
    i += 1
print(sum(fibo_nums))