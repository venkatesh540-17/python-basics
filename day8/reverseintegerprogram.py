def reverse(x:int)->int:
    rev=0
    sign=-1 if x<0 else 1
    x=abs(x)

    while x>0:
        rem=x%10
        rev=rev*10+rem
        x=x//10
    return rev*sign
x=int(input("enter the number"))
res=reverse(x)
print(res)



