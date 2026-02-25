from math import sqrt

num = 197
if num<=1:
    print("wrong input")
isprime = True
#for i in range(2,int(num**0.5+1)):
for i in range(2,int(sqrt(num+1))):
    if num%i==0:
        isprime=False

print(isprime)
