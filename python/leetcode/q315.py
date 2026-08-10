from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        # Store (value, original_index)
        arr = [(nums[i], i) for i in range(n)]

        def merge_sort(left, right):
            if right - left <= 1:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid, right)

            temp = []
            i, j = left, mid
            smaller = 0

            while i < mid and j < right:
                if arr[j][0] < arr[i][0]:
                    temp.append(arr[j])
                    smaller += 1
                    j += 1
                else:
                    result[arr[i][1]] += smaller
                    temp.append(arr[i])
                    i += 1

            while i < mid:
                result[arr[i][1]] += smaller
                temp.append(arr[i])
                i += 1

            while j < right:
                temp.append(arr[j])
                j += 1
