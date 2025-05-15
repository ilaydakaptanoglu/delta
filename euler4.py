from ourlib import *

prod_list = []
for i in range(100, 1000):
    for j in range(100, 1000):
        prod = i*j
        if poli(prod):
            prod_list.append(prod)

print(max(prod_list))