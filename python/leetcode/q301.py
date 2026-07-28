from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            balance = 0
            for ch in string:
                if ch == "(":
                    balance += 1
                elif ch == ")":
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        level = {s}

        while True:
            valid = [string for string in level if is_valid(string)]
            if valid:
                return valid
