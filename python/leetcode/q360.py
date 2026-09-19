class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def f(x):
            return a * x * x + b * x + c

        n = len(nums)
        ans = [0] * n

        left, right = 0, n - 1

        if a >= 0:
            # Largest values come from the ends
            pos = n - 1

            while left <= right:
                l = f(nums[left])
                r = f(nums[right])

                if l > r:
                    ans[pos] = l
                    left += 1
                else:
                    ans[pos] = r
                    right -= 1

                pos -= 1
        else:
            # Smallest values come from the ends
            pos = 0

            while left <= right:
                l = f(nums[left])
                r = f(nums[right])

                if l < r:
                    ans[pos] = l
                    left += 1
                else:
                    ans[pos] = r
                    right -= 1

                pos += 1

        return ans