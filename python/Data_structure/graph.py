from collections import deque

graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}

def bfs(start):
    visited = set()
    q = deque([start])

    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            q.extend(graph[node])

bfs(1)  # 1 2 3 4
