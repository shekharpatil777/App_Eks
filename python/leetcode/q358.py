class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        def f(x):
            return a * x * x + b * x + c

        n = len(nums)
        ans = [0] * n

        left, right = 0, n - 1

        # Parabola opens upward → largest values at the ends
        if a > 0:
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

        # Parabola opens downward → smallest values at the ends
        else:
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