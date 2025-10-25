iclass Solution:
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
                

        
        # The string is valid only if the stack is empty at the end.
        # An empty stack means all opening brackets were properly closed.
        return not stack