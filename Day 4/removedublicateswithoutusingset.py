l1=[2,2,4,5,3,4,5,6,7,6,5,6,7,8,9]
res=[]
start=0
for num in l1:
    if num not in res:
        res.append(num)
    else:
        num=num+1
print(res)