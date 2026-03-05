str= "a1b2c3"
#output=123abc

res=""
alpha=""
for s in str:
    if s.isdigit():
        res+=s
    else:
        alpha+=s
print(res+alpha)