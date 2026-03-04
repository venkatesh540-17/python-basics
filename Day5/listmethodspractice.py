list1=[7,6,6,7,8,5,5,4,3,2]
list1.append(50)      # Add at end
list1.insert(1, 15)   # Insert at index
print(list1)

list1.pop() # pop last num

list2=[6,5,4,3]
print(list1+list2) #merge two lists

list1.remove(7)   #remove by value
list1.pop()        #remove last element
del list1[0]       #delete by index
print(list1)

list3=set(list1)
print(list3) #removedublicates

#sortlist
sortd=list1.sort()
print(list1)

asessort=list1.sort(reverse=True)
print(list1)
