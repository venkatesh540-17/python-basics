input=[123,34,12,543,55]
res=[]
for num in input:
    total=0
    for n in str(num):
        total+=int(n)

    res.append(total)
print(res)

