def longest(input):
    left=0
    maxlen=0
    charset=set()
    result=""

    for right in range(len(input)):
        while input[right] in charset:
            charset.remove(input[left])
            left+=1
        charset.add(input[right])
        if right - left + 1>maxlen:
            maxlen=right - left + 1
            result=input[left:right+1]

    #return (maxlen)
    return(result)

print(longest("abcdacca"))
