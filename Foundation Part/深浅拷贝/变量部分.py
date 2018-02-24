bar = 1
print(id(bar))
foo = bar
print(id(foo))
bar = 2
print(id(bar))
print(id(foo))
