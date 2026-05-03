class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # 'prev2' represents f(i-2), 'prev1' represents f(i-1)
        prev1 = 0
        prev2 = 0
        
        for num in nums:
            # Calculate max profit at current house
            current = max(prev1, num + prev2)
