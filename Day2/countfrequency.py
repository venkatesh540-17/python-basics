str="venkatesh"
res={}
for s in str:
    res[s]=res.get(s,0)+1
print(res)
