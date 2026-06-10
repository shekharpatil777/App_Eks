from typing import List
from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        @lru_cache(None)
        def solve(expr):
            result = []

            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i + 1:])

                    for l in left:
                        for r in right:
                            if ch == '+':
                                result.append(l + r)
                            elif ch == '-':
                                result.append(l - r)
                            else:
                                result.append(l * r)

            if not result:
                result.append(int(expr))

            return result

        return solve(expression)