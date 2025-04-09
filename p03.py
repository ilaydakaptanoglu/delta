#random numbers
import random

# def fonksiyon yapmak icin kullan 

def thebiggest(a, b, c):
    nums = []
    nums.append(a)
    nums.append(b)
    nums.append(c)
    
    m = max(nums)
    
    return m

a = random.randint(1,100)
b = random.randint(1,100)
c = random.randint(1,100)

print(f"The max value is {thebiggest(a,b,c)}.")

'''
a = random.randint(1, 100)
print(a)

# ilk random kutuphane ikincisi fonksiyon
# random fonksiyonu her sayiyi karsina cikarir

b = random.randint(1, 100)
print(b)
c = random.randint(1, 100)
print(c)

nums = []
nums.append(a)
nums.append(b)
nums.append(c)

m = max(nums)
print(f"The max value of this random number is {m}.")
'''