digit=123445
sum=0
while digit>0:
    rem=digit%10
    sum=sum+rem
    digit=digit//10

print(sum)