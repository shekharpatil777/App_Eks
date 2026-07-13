from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def backtrack(
            index: int,
            expression: str,
            value: int,
            previous: int
        ) -> None:
            # All digits have been used
            if index == len(num):
                if value == target:
                    result.append(expression)
                return

            for end in range(index, len(num)):
                # Numbers such as "05" are not allowed
                if end > index and num[index] == "0":
                    break

                current_str = num[index:end + 1]
                current = int(current_str)

                # First number: no operator before it
                if index == 0:
                    backtrack(
                        end + 1,
                        current_str,
                        current,
                        current
                    )
                else:
                    # Addition
                    backtrack(
                        end + 1,
                        expression + "+" + current_str,
                        value + current,
                        current
                    )

                    # Subtraction
                    backtrack(
                        end + 1,
                        expression + "-" + current_str,
                        value - current,
                        -current
                    )

                    # Multiplication
                    multiplied_value = value - previous + previous * current

                    backtrack(
                        end + 1,
                        expression + "*" + current_str,
                        multiplied_value,
                        previous * current
                    )

        backtrack(0, "", 0, 0)
        return result