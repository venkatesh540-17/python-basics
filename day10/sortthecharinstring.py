str1="venkatesh"
l = list(str1)

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

result = ''.join(l)
print(result)