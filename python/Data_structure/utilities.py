import itertools as it
import operator

# accumulate (running totals/products)
print(list(it.accumulate([1, 2, 3, 4], operator.add)))
# [1, 3, 6, 10]

# chain
print(list(it.chain("ABC", "XYZ")))
# ['A', 'B', 'C', 'X', 'Y', 'Z']


