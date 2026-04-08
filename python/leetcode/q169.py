class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            # If count is 0, we pick a new candidate
            if count == 0:
                candidate = num
            
            # If current num matches candidate, increment; else decrement
            count += (1 if num == candidate else -1)

        return candidate