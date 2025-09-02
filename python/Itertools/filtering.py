import itertools as it

# compress(data, selectors)
print(list(it.compress('ABCDEF', [1, 0, 1, 0, 1, 1])))
# ['A', 'C', 'E', 'F']

# dropwhile(predicate, iterable)
print(list(it.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 7])))
# [6, 4, 7]


