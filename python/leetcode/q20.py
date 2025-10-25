class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map closing brackets to their corresponding opening brackets
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        
        # Initialize an empty stack (a list in Python)
        stack = []
        
        for char in s:
            if char in close_to_open:
                # Character is a closing bracket
                
                # 1. Check if the stack is NOT empty AND the top element of the stack
                #    is the matching opening bracket.
                if stack and stack[-1] == close_to_open[char]:
                    # Match found, pop the opening bracket
                    stack.pop()
                else:
                    # Mismatch (e.g., ']' and stack top is '(') or stack is empty
                    return False
            else:
                # Character is an opening bracket, push it onto the stack
                stack.append(char)
        
        # The string is valid only if the stack is empty at the end.
        # An empty stack means all opening brackets were properly closed.
        return not stack