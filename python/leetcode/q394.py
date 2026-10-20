class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                # Push the current accumulated string and repeat multiplier
                stack.append((curr_str, curr_num))
                # Reset for the content inside the brackets
                curr_str = ""
                curr_num = 0
            elif char == ']':
                # Pop previous context and multiply the inner string
                prev_str, repeat_count = stack.pop()
                curr_str = prev_str + repeat_count * curr_str
            else:
                curr_str += char

        return curr_str