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

                if not stack:
                    # If the stack is empty after popping, it means the current ')' 
                    # is unmatched. Push its index to be the new base.
                    stack.append(i)
                else:
                    # If the stack is not empty, a valid pair is formed.
                    # The length of the current valid substring is (current index) - (new top index).
                    # The new top index represents the index right before the current valid substring.
                    current_length = i - stack[-1]
                    max_length = max(max_length, current_length)
        
        return max_length

# Example Usage:
# sol = Solution()
# print(f"Input: '(()', Output: {sol.longestValidParentheses('(()')}")  # Output: 2
# print(f"Input: ')()()', Output: {sol.longestValidParentheses(')()()')}") # Output: 4