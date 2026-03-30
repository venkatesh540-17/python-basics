lst=[1,2,0,-1,-4,-5,0,4,0,0,3,0,-7]
pos=0
for i in range(len(lst)):
    if lst[i]<0:
        temp=lst[i]
        j=i

        while j>pos:
            lst[j]=lst[j-1]
            j-=1

        lst[pos]=temp
        pos+=1
for i in range(pos,len(lst)):
    if lst[i]==0:
        temp=lst[i]
        j=i

        while j>pos:
            lst[j]=lst[j-1]
            j-=1
        lst[pos]=temp
        pos+=1
print(lst)


