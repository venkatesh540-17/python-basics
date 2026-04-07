import copy

original = [[1, 2], [3, 4]]

shallow=copy.copy(original)
deep=copy.deepcopy(original)

shallow[0][0] = 100
deep[1][1] = 200

print("Original",original)
print("shallow",shallow)
print("deep",deep)