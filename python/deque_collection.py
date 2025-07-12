from collections import deque

#A double-ended queue (fast append and pop from both ends).
dq = deque()
dq.append('a')
dq.appendleft('b')
print(dq)  # deque(['b', 'a'])
dq.pop()      # 'a'
dq.popleft()  # 'b'
