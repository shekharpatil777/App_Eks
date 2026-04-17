from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Convert numbers to strings
        nums = list(map(str, nums))
        
        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1   # a should come first
            elif a + b < b + a:
                return 1    # b should come first
            else:
                return 0
        
        # Sort using custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join result
        result = ''.join(nums)
        
        # Edge case: leading zeros
        return '0' if result[0] == '0' else result