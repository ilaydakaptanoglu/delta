'''
#def poli(n):
#   return True

s = "ala ma"
d = len(s)
print(d)

for i in range(d):
    print(s[i])

print(type(s))

li = list(s)
print(s)
print(li)

# ala ma
print(s[1])

print(li[4])
'''

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


print(poli(134))
