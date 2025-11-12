from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Initialize hash maps for rows, columns, and 3x3 squares
        # The key for squares will be a tuple (r // 3, c // 3)
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # Key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                char = board[r][c]

                # Skip empty cells
                if char == ".":
                    continue

                # 1. Check for duplicates in the current row
                # 2. Check for duplicates in the current column
                # 3. Check for duplicates in the current 3x3 square
                # The sub-box key is calculated using integer division:
                # (0,0) to (2,2) -> (0,0)
                # (0,3) to (2,5) -> (0,1)
                # (3,0) to (5,2) -> (1,0)
                
                if (char in rows[r] or 
                    char in cols[c] or 
                    char in squares[(r // 3, c // 3)]):
                    return False

                # If no duplicates found, add the character to the respective sets
                rows[r].add(char)
                cols[c].add(char)
                squares[(r // 3, c // 3)].add(char)

