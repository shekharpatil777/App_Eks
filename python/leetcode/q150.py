class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for char in tokens:
            if char not in "+-*/":
                stack.append(int(char))
            else:
                # The first pop is the right operand, second is left
                right = stack.pop()
                left = stack.pop()
                
                if char == "+":
                    stack.append(left + right)
                elif char == "-":
                    stack.append(left - right)
                elif char == "*":
                    stack.append(left * right)
