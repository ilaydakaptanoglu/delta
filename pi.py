def leib(n):
  pi = 0.0
  for i in range(0, n+1):
    pi += (-1) ** i / (2 * i + 1)
  pi *= 4
  return pi

print(leib(100000))

import matplotlib.pyplot as plt
plt.style.use('bmh')

def calculate_pi(n):
  y = []
  x = []
  z = []
  s = 0
  for i in range(1, n+1):
    s = s + 1.0*(-1)**(i+1)*4/(2*i-1)
    x.append(i)
    y.append(round(s,2))
    z.append(3.14)
  return x, y, z

x, y, z = calculate_pi(100)
#print(x)
#print(y)
#print(z)

fig,ax = plt.subplots() #preparetion of different aspects pf chart
ax.plot(y, c='blue')
ax.plot(z, c='red')

ax.set_title("Aproaching to number PI ", fontsize=12)
ax.set_xlabel('Number of iterations', fontsize=12)
ax.set_ylabel("Calculated value of PI", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=8)
plt.show()

'''
import matplotlib.pyplot as plt
import math

plt.style.use('bmh')

def calculate_pi(n):
    y = []
    x = []
    z = []
    s = 0
    for i in range(1, n+1):
        s = s + 1.0*(-1)**(i+1)*4/(2*i-1)
        x.append(i)
        y.append(round(s,2))
        z.append(3.14)
    return x, y, z

def calculate_pi_euler(n):
    y = []
    s = 0
    for i in range(1, n+1):
        s += 1 / (i ** 2)
        approx = math.sqrt(6 * s)
        y.append(round(approx, 2))
    return y

def calculate_pi_wallis(n):
    y = []
    product = 1
    for i in range(1, n + 1):
        product *= (4 * i ** 2) / (4 * i ** 2 - 1)
        approx = round(product * 2, 2)
        y.append(approx)
    return y


x, y_leib, z = calculate_pi(20)
y_euler = calculate_pi_euler(20)
y_wallis = calculate_pi_wallis(20)

# for chart ilayda kaptanoğlu
fig, ax = plt.subplots()
ax.plot(y_leib, c='yellow', label='Leibniz')
ax.plot(z, c='blue', label='Sabit 3.14')
ax.plot(y_euler, c='black', label='Euler')
ax.plot(y_wallis, c='green', label='Wallis')

ax.set_title("Approaching to number PI", fontsize=12)
ax.set_xlabel('Number of iterations: ' + str(len(x)), fontsize=12)
ax.set_ylabel("Calculated value of PI", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=8)
ax.legend(bbox_to_anchor=(1, 1), ncol=4)
plt.show()
'''