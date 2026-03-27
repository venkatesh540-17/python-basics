arr = [2,9,5,6,2,1]
target = 11

seen = set()
sub = []

for num in arr:
    if target - num in seen:
        sub.append((target - num, num))
    seen.add(num)

print(sub)