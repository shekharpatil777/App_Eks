from collections import defaultdict

dd = defaultdict(int)
dd['a'] += 1
print(dd)  # defaultdict(<class 'int'>, {'a': 1})
