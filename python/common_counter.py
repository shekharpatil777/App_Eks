from collections import Counter

words = "a a b b b c".split()
counter = Counter(words)
print(counter.most_common(2))
