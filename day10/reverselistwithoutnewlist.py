l1 = [2, 3, 4, 5, 6]
start = 0
end = len(l1) - 1

while start < end:
    l1[start], l1[end] = l1[end], l1[start]
    start += 1
    end -= 1

print(l1)