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
