from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        result = []

        for i in range(len(nums)):
            # Remove indices outside current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
