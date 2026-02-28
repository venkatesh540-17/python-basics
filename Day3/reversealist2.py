l1=[5,3,4,2,6,9]
# o/p: [9,6,2,4,3,5]
start=0;
end=len(l1)-1
while end>start:
    l1[start],l1[end]=l1[end],l1[start]
    start+=1
    end-=1
print(l1)