from itertools import cycle

count = 0
for item in cycle(['A', 'B', 'C']):
    if count > 6:
        break
    print(item, end=" ")  # A B C A B C A
    count += 1
