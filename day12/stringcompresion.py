word="aabbccddd"
#output=a2b2c3
result=""
count=1
for i in range(1,len(word)):
    if word[i]==word[i-1]:
        count = count + 1
    else:
        result+=word[i-1]+str(count)
        count=1
result+=word[-1]+str(count)
print(result)