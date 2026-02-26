list=[2,1,3,2,5,4,3,2,5,7]
res=[]
for num in list:
    if num not in  res:
        res.append(num)
print(res)
