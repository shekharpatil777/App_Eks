from itertools import compress

data = ['a', 'b', 'c', 'd']
selectors = [1, 0, 1, 0]
print(list(compress(data, selectors)))  # ['a', 'c']
