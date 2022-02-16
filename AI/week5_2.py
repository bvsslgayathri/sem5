import math
from itertools import permutations

def fun(a):
    sum1 = 0
    p = 0
    for x in a[::-1]:
        sum1 += d[x]*int(math.pow(10,p))
        p+=1
    return sum1

a = input("Enter the string 1 : ")
b = input("Enter the string 2 : ")
r = input("Enter the result   : ")
d = {}
for x in a+b+r:
    if x not in d.keys():
        d[x] = 0
print(d)
perm = permutations([0,1,2,3,4,5,6,7,8,9],len(d))
for i in list(perm):
    index = 0
    for x in d.keys():
        d[x] = i[index]
        index+=1
    x,y,z = fun(a),fun(b),fun(r)
    if x+y == z:
        print(x,y,z)
