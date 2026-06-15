class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mp = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        left, right = 0, len(num) - 1
