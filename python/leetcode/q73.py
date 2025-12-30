class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        # 1. Check if first row has any zero
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        # 2. Check if first column has any zero
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # 3. Use first row and column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 4. Use markers to set elements to zero
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0


        # 5. Handle the first row
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # 6. Handle the first column
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0