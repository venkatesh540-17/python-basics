nums=[1,2,3,4,5]
target=5
pairs=[]
seen=set()

for num in nums:
    complement=target-num
    if complement in seen:
        pairs.append((complement,num))
    seen.add(num)
print(pairs)