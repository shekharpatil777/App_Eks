from collections import ChainMap

#Groups multiple dicts together
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
cm = ChainMap(dict1, dict2)
print(cm['b'])  # 2 (from dict1, first dict)
