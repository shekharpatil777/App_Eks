import itertools as it

# compress(data, selectors)
print(list(it.compress('ABCDEF', [1, 0, 1, 0, 1, 1])))
# ['A', 'C', 'E', 'F']

# dropwhile(predicate, iterable)
print(list(it.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 7])))
# [6, 4, 7]

# takewhile(predicate, iterable)
print(list(it.takewhile(lambda x: x < 5, [1, 4, 6, 4, 7])))
# [1, 4]

# filterfalse(predicate, iterable)
print(list(it.filterfalse(lambda x: x % 2, range(10))))
# [0, 2, 4, 6, 8]

