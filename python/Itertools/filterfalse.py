from itertools import filterfalse

nums = [1, 2, 3, 4, 5]
print(list(filterfalse(lambda x: x % 2, nums)))  # [2, 4]
