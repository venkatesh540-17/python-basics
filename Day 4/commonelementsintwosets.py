s1={1,2,3,4}
s2={6,7,8,1,2}
res=[]
for i in s1:
    if i in s2:
        res.append(i)
print(res)