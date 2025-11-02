class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
