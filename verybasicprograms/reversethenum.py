num=12345
result=0

while num>0:
    rem=num%10
    result=result*10+rem
    num=num//10

print(result)