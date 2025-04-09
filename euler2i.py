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
    return next

fibo_nums = fibo_i(10)
print(fibo_nums)
