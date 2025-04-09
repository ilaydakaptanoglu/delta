import random


def fibo(n):
    if n < 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibo_i(n):
    a = 1
    b = 2
    next = 0
    fibo_nums = [1, 2]

    for i in range(3, n+1):
        next = a + b
        a = b
        b = next
        fibo_nums.append(next)
    return fibo_nums

def thebiggest(a, b, c):
    nums.append(a)
    nums.append(b)
    nums.append(c)
    m = max(nums)
    return m 