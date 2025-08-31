data = [("cat", 2), ("dog", 1), ("cat", 4), ("dog", 3)]
for k, g in it.groupby(sorted(data, key=lambda x: x[0]), key=lambda x: x[0]):
    print(k, list(g))