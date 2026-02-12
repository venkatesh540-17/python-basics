from collections import Counter
#method ---1
elements = ["Pass", "Fail", "Pass", "Skip", "Fail", "Pass"]

result = Counter(elements)
print(result)

#METHOD--2

result={}

for item in elements:
    result[item]=result.get(item,0)+1
    # if item in result:
    #     result[item]+=1
    # else :
    #     result[item]=1
print(result)

#method--3

