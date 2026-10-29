class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            # Maintain a monotonic increasing order
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        # If k is still greater than 0, truncate from the end
        if k > 0:
            stack = stack[:-k]
