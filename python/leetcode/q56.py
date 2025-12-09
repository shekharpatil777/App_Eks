from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the intervals by their start time.
        # This is the key step, making all overlapping intervals adjacent.
        intervals.sort()

        # Initialize the result list with the first interval.
        merged = []
        
        for interval in intervals:
            # Case 1: The result list is empty, or the current interval does not overlap
            # with the last merged interval.
            # No overlap exists if the current interval's start (interval[0]) 
            # is greater than the end of the last merged interval (merged[-1][1]).
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            
            # Case 2: There is an overlap, so merge by updating the end time 
            # of the last merged interval.
            # The new end time is the maximum of the current end time and 
            # the new interval's end time.
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged