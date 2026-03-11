class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            # Update 'ones' only if the bit isn't already in 'twos'
            ones = (ones ^ num) & ~twos
            
            # Update 'twos' only if the bit isn't already in the new 'ones'
            twos = (twos ^ num) & ~ones
            
        return ones