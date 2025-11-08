class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize the maximum length found so far
        max_length = 0
        # Initialize a stack with -1. This serves as a base index 
        # for calculating the length of valid substrings.
        stack = [-1] 

        for i, char in enumerate(s):
            if char == '(':
                # Push the index of '(' onto the stack
                stack.append(i)
            else:  # char == ')'
                # Pop the top element (index of the matching '(' or the base index)
                stack.pop()



# Example Usage:
# sol = Solution()
# print(f"Input: '(()', Output: {sol.longestValidParentheses('(()')}")  # Output: 2
# print(f"Input: ')()()', Output: {sol.longestValidParentheses(')()()')}") # Output: 4