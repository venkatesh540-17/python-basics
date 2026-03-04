list1=[5,4,4,3]
list2=[4,7,8,5,9,6,]
common=[]
for num in list1:
    if num in list2:
        common.append(num)
        list2.remove(num)
print(common)