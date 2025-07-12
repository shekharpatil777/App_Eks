from collections import deque

dq = deque()
dq.append('a')
dq.appendleft('b')
print(dq)  # deque(['b', 'a'])
dq.pop()      # 'a'
dq.popleft()  # 'b'
