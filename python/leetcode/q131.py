class Solution:
    def partition(self, s: str):
        res = []
        path = []

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return

