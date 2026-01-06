class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # k tracks the position for the next valid element
        k = 0
        for x in nums:
            # We add the element if:
            # 1. We have added fewer than 2 elements total (k < 2)

                
        return k
