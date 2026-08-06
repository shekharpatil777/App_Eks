from typing import List


class Solution:
    def multiply(
        self,
        mat1: List[List[int]],
        mat2: List[List[int]]
    ) -> List[List[int]]:
        rows = len(mat1)
        common = len(mat2)
        cols = len(mat2[0])

        result = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for k in range(common):
                if mat1[i][k] == 0:
                    continue

                for j in range(cols):
                    if mat2[k][j] != 0:
                        result[i][j] += mat1[i][k] * mat2[k][j]

        return result