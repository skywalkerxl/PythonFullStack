import copy

a = [[1, 2], 3, 4, 5]

print(id(a))
print(id(a[0]), id(a[1]), id(a[2]), id(a[3]))
print("")

# b = a.copy()
b = copy.deepcopy(a)
print(id(b))
print("b:", id(b[0]), id(b[1]), id(b[2]), id(b[3]))
print("")
print("a:", id(a[0]), id(a[1]), id(a[2]), id(a[3]))
print("")

