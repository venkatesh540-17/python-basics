input=[32,222,333,444,555]
result=[]
for num in input:
    total = 0

    for n in str(num):

        total=total+int(n)
    result.append(total)
print(result)
