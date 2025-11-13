class Solution:


            # Check 3x3 sub-box
            start_r, start_c = 3 * (r // 3), 3 * (c // 3)
            for i in range(start_r, start_r + 3):
                for j in range(start_c, start_c + 3):
                    if board[i][j] == ch:
                        return False
            return True

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for ch in '123456789':
                            if is_valid(r, c, ch):
                                board[r][c] = ch
                                if solve():
                                    return True
                                board[r][c] = '.'
                        return False
            return True

        solve()
