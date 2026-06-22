from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        heap = [intervals[0][1]]  # end time of first meeting

        for start, end in intervals[1:]:
            if start >= heap[0]:
                heapq.heappop(heap)  # reuse room

            heapq.heappush(heap, end)

        return len(heap)