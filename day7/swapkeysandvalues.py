data = {"a": 1,"b": 2,"c": 3}
inverted = {}
for key, value in data.items():
    inverted[value] = key

print(inverted)