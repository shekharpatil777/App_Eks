import itertools as it
import operator

# accumulate (running totals/products)
print(list(it.accumulate([1, 2, 3, 4], operator.add)))
# [1, 3, 6, 10]

# chain
print(list(it.chain("ABC", "XYZ")))
# ['A', 'B', 'C', 'X', 'Y', 'Z']

# islice(iterable, start, stop, step)
print(list(it.islice(range(10), 2, 8, 2)))
# [2, 4, 6]

# starmap(function, iterable)
print(list(it.starmap(pow, [(2, 5), (3, 2), (10, 3)])))
# [32, 9, 1000]
