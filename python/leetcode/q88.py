class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set pointers for nums1, nums2, and the end of nums1's total capacity
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        # While there are elements in both arrays to compare
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If nums2 still has elements left (nums1 elements are already in place)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1