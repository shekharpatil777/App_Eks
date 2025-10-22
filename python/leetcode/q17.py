class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        digit_to_chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []



        backtrack(0, [])
        return res
