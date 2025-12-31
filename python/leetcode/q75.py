class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # Swap mid with low to move the 0 to the front
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is already in the "middle" zone, just move forward
                mid += 1
            else: # nums[mid] == 2
                # Swap mid with high to move the 2 to the end
                nums[mid], nums[high] = nums[high], nums[mid]
                # Decrement high, but DON'T increment mid yet 
                # because the new nums[mid] needs to be checked.
                high -= 1