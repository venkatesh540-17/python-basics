l1=["cat", "act", "tac", "listen", "silent", "nat","tan"]
grouped={}
for word in l1:
    key="".join(sorted(word))
    if key in grouped:
         grouped[key].append(word)
    else:
        grouped[key]=[word]
print(grouped)
