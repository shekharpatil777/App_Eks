from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        i = 0

        # 1. Add all non-overlapping intervals that end before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        # 2. Merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged newInterval to the result list
        ans.append(newInterval)

        # 3. Add all non-overlapping intervals that start after the merged interval ends
        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans