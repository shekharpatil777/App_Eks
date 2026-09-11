class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # skip[i][j] stores the intermediate number that must be visited
        # before jumping from i to j.
        skip = [[0] * 10 for _ in range(10)]
        
        # Horizontal & Vertical jumps
        skip[1][3] = skip[3][1] = 2
        skip[7][9] = skip[9][7] = 8
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        
        # Diagonal and center-crossing jumps
        skip[1][9] = skip[9][1] = 5
        skip[3][7] = skip[7][3] = 5
        skip[2][8] = skip[8][2] = 5
        skip[4][6] = skip[6][4] = 5
        
        visited = [False] * 10
        
        def dfs(curr: int, remaining_steps: int) -> int:
            if remaining_steps == 1:
                return 1
            
            visited[curr] = True
            count = 0
            
            for nxt in range(1, 10):
                # Valid if next node is unvisited and either:
                # - No intermediate node exists (skip[curr][nxt] == 0)
                # - Intermediate node is already visited
                if not visited[nxt]:
                    mid = skip[curr][nxt]
                    if mid == 0 or visited[mid]:
                        count += dfs(nxt, remaining_steps - 1)
                        
            visited[curr] = False
            return count

        total_patterns = 0
        for length in range(m, n + 1):
            # Symmetry optimization:
            # 1, 3, 7, 9 are corners (4-fold symmetry)
            # 2, 4, 6, 8 are edge centers (4-fold symmetry)
            # 5 is the center (unique)
            total_patterns += 4 * dfs(1, length)
            total_patterns += 4 * dfs(2, length)
            total_patterns += dfs(5, length)
            
        return total_patterns