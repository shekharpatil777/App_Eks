from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        # Pair each number with its original index: (val, original_idx)
        indexed_nums = list(enumerate(nums))

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            merged = []
            i = j = 0
            right_count = 0

            while i < len(left) and j < len(right):
                # If element from right is strictly smaller, advance right pointer
                if right[j][1] < left[i][1]:
                    right_count += 1
                    merged.append(right[j])
                    j += 1
                else:
                    # Element from left is <= right[j], so all previously placed 
                    # elements from right (right_count) are strictly smaller than left[i]
                    counts[left[i][0]] += right_count
                    merged.append(left[i])
                    i += 1

            # Drain remaining left elements
            while i < len(left):
                counts[left[i][0]] += right_count
                merged.append(left[i])
                i += 1
