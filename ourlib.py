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

def is_prime(n):
    prime = True
    if n < 2:
        prime = False
        return prime
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    return prime

def poli(num):
     s = ''
     num_l = list(str(num))
     d = len(num_l)

     for i in range(d//2):
         tmp = num_l[i]
         #print(tmp)
         num_l[i] = num_l[d-1-i]
         num_l[d-1-i] = tmp
     for i in range(d):
         s += num_l[i]

     num2 = int(s)
     return (num == num2)