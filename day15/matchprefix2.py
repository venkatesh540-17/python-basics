def matchingprefix(input):
    prefix=input[0]
    for word in input[1:]:
        while not word.endswith(prefix):
            prefix=prefix[1:]
            if prefix=="":
                return""
    return prefix
input=["running", "jogging", "walking"]
print(matchingprefix(input))