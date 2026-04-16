def primenum(num):
    for i in range(2,int(num**0.5)+1):
        if num%i**.5+1==0:
            return False
        return True

count=0
num=2

while count<5:
    if primenum(num):
        print(num)
        count+=1
    num+=1