list1=[1,2,3,-1,-2,-3,-4,5]
for num in list1[:]:
    if num<0:
        list1.remove(num)
print(list1)