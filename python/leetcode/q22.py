class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(s="", left=0, right=0):
            # If string length == total possible pairs × 2 → add to result
            if len(s) == 2 * n:
                res.append(s)
                return

            # Can add '(' if we still have left brackets available
            if left < n:
                backtrack(s + "(", left + 1, right)

            # Can add ')' only if there are unmatched '('
            if right < left:
                backtrack(s + ")", left, right + 1)

        backtrack()
        return res
