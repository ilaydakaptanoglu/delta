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

print(is_prime(49))

for i in range(2, 100):
    print(f"{i} is prime number? -----> {is_prime(i)}")

'''
def is_prime(n):
    prime = True
'''