list1=[4,0,5,0,4,0,1,2,3,0,4,5,4]
list2=[]
list3=[]
for num in list1:
    if num==0:
        list3.append(num)
    else:
        list2.append(num)
print(list2+list3)