class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # k tracks the position for the next valid element
        k = 0
        for x in nums:
            # We add the element if:
            # 1. We have added fewer than 2 elements total (k < 2)
            # 2. The current element is different from the one 2 spots back 
            if k < 2 or x != nums[k - 2]:
                nums[k] = x
                k += 1
                
        return k
