import copy

a=([2,1],[4,3])
b=copy.copy(a)
b[0][0]=7
print(a)
print(b)

c=([2,1],[4,3])
d=copy.deepcopy(c)
d[0][0]=8
print(c)
print(d)