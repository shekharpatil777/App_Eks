from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(
        self, 
        equations: List[List[str]], 
        values: List[float], 
        queries: List[List[str]]
    ) -> List[float]:
        # Step 1: Build the directed graph
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val

        def bfs(start: str, end: str) -> float:
            # If either variable has never been seen, division is undefined
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            queue = deque([(start, 1.0)])
            visited = {start}

            while queue:
                curr_node, curr_prod = queue.popleft()
                if curr_node == end:
                    return curr_prod

                for neighbor, weight in graph[curr_node].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, curr_prod * weight))

            return -1.0

        # Step 2: Process each query
        return [bfs(q[0], q[1]) for q in queries]