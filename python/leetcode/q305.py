from typing import List


class Solution:
    def numIslands2(
        self,
        m: int,
        n: int,
        positions: List[List[int]]
    ) -> List[int]:

        parent = {}
        rank = {}
        islands = 0
        answer = []

        def find(node):
            # Path compression
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            nonlocal islands

            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return

            # Union by rank
            if rank[root1] < rank[root2]:
                root1, root2 = root2, root1

            parent[root2] = root1

            if rank[root1] == rank[root2]:
                rank[root1] += 1

            islands -= 1

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        for row, col in positions:
            cell = (row, col)

            # Duplicate land addition
            if cell in parent:
                answer.append(islands)
                continue

            parent[cell] = cell
            rank[cell] = 0
            islands += 1

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                neighbour = (new_row, new_col)

                if (
                    0 <= new_row < m
                    and 0 <= new_col < n
                    and neighbour in parent
                ):
                    union(cell, neighbour)

            answer.append(islands)

        return answer