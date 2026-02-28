l1=[5,3,4,2,6,9]
# o/p: [2,3,4,5,6,9]
len=len(l1)-1
for i in range(0,len):
    for j in range(0,len-1-i):
        if l1[j]>l1[j+1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]

print(l1)