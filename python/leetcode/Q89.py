class Solution:
    def grayCode(self, n: int) -> list[int]:
        # Start with the base case for n = 0
        result = [0]
        
        for i in range(n):
            # The value to add to the mirrored part (2^i)
            mask = 1 << i
            
            # Iterate through the current result in reverse order
            # and add the mask to each element
            for j in range(len(result) - 1, -1, -1):
                result.append(result[j] | mask)
                
        return result