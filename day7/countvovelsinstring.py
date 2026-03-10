input="chennai"
vovels="aeiouAEIOU"
count=0
for char in input:

    if char in vovels:
        count+=1
print(count)