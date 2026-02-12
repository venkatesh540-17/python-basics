li = [2,3,4,5,6,7,8,8]

li.append(2)
li.insert(3,4)
li.pop()
print(li[::-1])
print(len(li))


arr = [1, 2, 3, 4, 5]
k = 3
print(arr[k:]+arr[:k])  # Rotate left by k
