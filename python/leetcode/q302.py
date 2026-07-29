from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        remove_left = 0
        remove_right = 0

        # Calculate the minimum parentheses to remove
        for char in s:
            if char == "(":
                remove_left += 1
            elif char == ")":
                if remove_left > 0:
                    remove_left -= 1
                else:
                    remove_right += 1

        result = set()

        def backtrack(
            index: int,
            left_count: int,
            right_count: int,
            left_rem: int,
            right_rem: int,
            path: list[str],
        ) -> None:
            if index == len(s):
                if (
                    left_rem == 0
                    and right_rem == 0
                    and left_count == right_count
                ):
                    result.add("".join(path))
                return

            char = s[index]

            # Option 1: Remove the current parenthesis
            if char == "(" and left_rem > 0:
                backtrack(
                    index + 1,
                    left_count,
                    right_count,
                    left_rem - 1,
                    right_rem,
                    path,
                )

            elif char == ")" and right_rem > 0:
                backtrack(
                    index + 1,
                    left_count,
                    right_count,
                    left_rem,
                    right_rem - 1,
                    path,
                )

            # Option 2: Keep the current character
            path.append(char)

            if char == "(":
                backtrack(
                    index + 1,
                    left_count + 1,
                    right_count,
                    left_rem,
                    right_rem,
                    path,
                )

            elif char == ")":
                # A closing bracket can only be kept if
                # there is an unmatched opening bracket
                if left_count > right_count:
                    backtrack(
                        index + 1,
                        left_count,
                        right_count + 1,
                        left_rem,
                        right_rem,
                        path,
                    )

            else:
                backtrack(
                    index + 1,
                    left_count,
                    right_count,
                    left_rem,
                    right_rem,
                    path,
                )

            path.pop()

        backtrack(0, 0, 0, remove_left, remove_right, [])
        return list(result)