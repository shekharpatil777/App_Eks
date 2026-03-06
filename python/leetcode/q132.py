class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start):
            # Base Case: If we've reached the end of the string, 
            # the current path is a valid partition.
            if start == len(s):
                res.append(list(path))
                return

            # Explore all possible "cuts" from the current start position
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                

                if is_palindrome(substring):
                    path.append(substring)    # Choose
                    backtrack(end)            # Explore
                    path.pop()                # Un-choose (Backtrack)

        backtrack(0)
        return res