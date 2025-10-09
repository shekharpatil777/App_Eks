def convert(s: str, numRows: int) -> str:
    """
    Converts a string to a zigzag pattern and reads it line by line.

    Args:
        s: The input string.
        numRows: The number of rows for the zigzag pattern.

    Returns:
        The converted string.
    """
    # Edge case: if numRows is 1, the pattern is just a single line.
    if numRows == 1 or numRows >= len(s):
        return s

    # Create a list of strings to hold characters for each row.
    rows = [''] * numRows
    current_row = 0
    going_down = False  # Start by going up to flip to down at row 0

    # Iterate through each character in the string.
    for char in s:
        rows[current_row] += char
        
        # If we're at the top or bottom row, change direction.
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        
        # Move to the next row based on the direction.
        if going_down:
            current_row += 1
        else:
            current_row -= 1
            
    # Join all the row strings together.
    return "".join(rows)

# Example Usage:
input_string = "PAYPALISHIRING"
rows = 3
print(f"Input: s = \"{input_string}\", numRows = {rows}")
# Expected Output: "PAHNAPLSIIGYIR"
print(f"Output: \"{convert(input_string, rows)}\"")

rows = 4
print(f"\nInput: s = \"{input_string}\", numRows = {rows}")
# Expected Output: "PINALSIGYAHRPI"
print(f"Output: \"{convert(input_string, rows)}\"")