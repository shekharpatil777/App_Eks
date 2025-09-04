from itertools import dropwhile, takewhile

nums = [1, 4, 6, 2, 7, 8]

print(list(dropwhile(lambda x: x < 5, nums)))  # [6, 2, 7, 8]
print(list(takewhile(lambda x: x < 5, nums)))  # [1, 4]
