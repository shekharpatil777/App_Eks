class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        if not board or not board[0]:
            return 0

        rows, cols = len(board), len(board[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    # Skip if it is part of a battleship continuing from above
                    if r > 0 and board[r - 1][c] == "X":
                        continue
                    # Skip if it is part of a battleship continuing from the left
                    if c > 0 and board[r][c - 1] == "X":
                        continue
                    # This is the "head" (top-left) of a new battleship
                    count += 1

        return count