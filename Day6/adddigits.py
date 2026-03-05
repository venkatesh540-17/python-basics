str="a1b2c3"
res=0
for s in str:
    if s.isdigit():
        res+=int(s)
print(res)