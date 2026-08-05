from typing import List
from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # A single node is itself the root of the minimum height tree.
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Start with all leaf nodes.
        leaves = deque()

        for node in range(n):
            if degree[node] == 1:
                leaves.append(node)

        remaining_nodes = n

        # Remove leaves layer by layer until at most two nodes remain.
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count
