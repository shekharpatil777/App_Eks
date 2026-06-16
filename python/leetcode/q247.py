class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:
        def build(length, total):
            if length == 0:
                return [""]
            if length == 1:
                return ["0", "1", "8"]

            middle = build(length - 2, total)
            result = []

            for num in middle:
                if length != total:  # Avoid leading zero
                    result.append("0" + num + "0")

                result.append("1" + num + "1")
                result.append("6" + num + "9")
                result.append("8" + num + "8")
                result.append("9" + num + "6")

            return result

        return build(n, n)