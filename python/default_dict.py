from collections import defaultdict

#A dict with a default value for new keys.
dd = defaultdict(int)
dd['a'] += 1
print(dd)  # defaultdict(<class 'int'>, {'a': 1})
