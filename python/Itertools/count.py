from itertools import count

for i in count(10, 2):   # start=10, step=2
    if i > 20:
        break
    print(i, end=" ")   # 10 12 14 16 18 20
