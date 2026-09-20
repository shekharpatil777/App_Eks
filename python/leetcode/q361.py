class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        ans = 0
        col_hits = [0] * n

        for i in range(m):
            row_hits = 0

            for j in range(n):
                # Recalculate enemies in this row segment
                if j == 0 or grid[i][j - 1] == 'W':
                    row_hits = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            row_hits += 1
                        k += 1

                # Recalculate enemies in this column segment
                if i == 0 or grid[i - 1][j] == 'W':
                    col_hits[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            col_hits[j] += 1
                        k += 1

                if grid[i][j] == '0':
                    ans = max(ans, row_hits + col_hits[j])

        return ans