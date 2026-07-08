# The knows API is already defined for you.
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0

        # Step 1: Find possible celebrity
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        # Step 2: Verify candidate
        for i in range(n):
            if i == candidate:
                continue
