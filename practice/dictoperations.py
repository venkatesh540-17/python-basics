d1 = {"stud1":40,"stud2":35,"stud3":56}

print(d1.get("stud1"))
print(d1.keys())
print(d1.values())
d1.update({"stud4":44})

sorted_scores = dict(sorted(d1.items(),key=lambda kv:kv[1]))
print(sorted_scores)