from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            papers = n - mid  # papers with citations >= citations[mid]

            if citations[mid] >= papers:
                ans = papers
                right = mid - 1
            else:
                left = mid + 1

        return ans