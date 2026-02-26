list=[9,5,7,6,8,5]
length=len(list)-1

for i in range(length):
    for j in range(0,length-i):
            if list[j]>list[j+1]:
               list[j],list[j+1]=list[j+1],list[j]

print(list)