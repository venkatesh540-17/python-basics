input="mr lava kumar is not lava kumar he is mr kumar"
res={}
for word in input.split(" "):
    res[word]=res.get(word,0)+1
print(res)