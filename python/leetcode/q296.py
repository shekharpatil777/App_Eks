from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = []
        cols = []

        m, n = len(grid), len(grid[0])

        # Row-major traversal keeps rows sorted
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    rows.append(r)

        # Column-major traversal keeps columns sorted
        for c in range(n):
            for r in range(m):
                if grid[r][c] == 1:
                    cols.append(c)

        return self.get_distance(rows) + self.get_distance(cols)
