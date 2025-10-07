class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Converts a string to a zigzag pattern based on the number of rows.
        """
        # Edge case: If numRows is 1 or string is too short for zigzag,
        # the pattern doesn't change the string.
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of empty strings to represent each row.
        rows = [''] * numRows
        
        current_row = 0
        going_down = False # Will be flipped to True on the first character

        # Iterate through each character of the string.
        for char in s:
            # Append the character to the string of the current row.
            rows[current_row] += char

            # If we are at the top row (0) or the bottom row (numRows - 1),
            # we need to change direction.
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row based on the current direction.
            if going_down:
                current_row += 1
            else:
                current_row -= 1
        
        # Join all the row strings to get the final result.
        return "".join(rows)

# Example Usage:
solver = Solution()
print(f"Input: 'PAYPALISHIRING', 3 -> Output: '{solver.convert('PAYPALISHIRING', 3)}'")
# Expected: 'PAHNAPLSIIGYIR'

print(f"Input: 'PAYPALISHIRING', 4 -> Output: '{solver.convert('PAYPALISHIRING', 4)}'")
# Expected: 'PINALSIGYAHRPI'


print(f"Input: 'A', 1 -> Output: '{solver.convert('A', 1)}'")
# Expected: 'A'