from collections import Counter

#Most Common Elements Using Counter
words = "a a b b b c".split()
counter = Counter(words)
print(counter.most_common(2))
