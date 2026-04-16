n=153
result=0
while n>0:
    rem=n%10
    result+=rem*rem*rem
    n=n//10
print(result)

