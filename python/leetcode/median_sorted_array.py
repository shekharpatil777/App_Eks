import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Finds the median of two sorted arrays using an optimized binary search approach.
        The time complexity is O(log(min(m, n))).
        The space complexity is O(1).
        """
        # Ensure nums1 is the smaller array to optimize binary search range.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low = 0
        high = m
        
        # Total elements and desired size of the combined left partition.
        # The +1 handles both even and odd total lengths correctly.
        total_length = m + n
        half_len = (total_length + 1) // 2

        while low <= high:
            # partitionX is the partition point in the smaller array (nums1).
            partitionX = (low + high) // 2
            # partitionY is calculated based on partitionX to maintain equal halves.
            partitionY = half_len - partitionX

            # Get the four boundary elements for the partitions.
            # Use -inf and +inf for edge cases where a partition is at the start or end.
            maxLeftX = nums1[partitionX - 1] if partitionX != 0 else -math.inf
            minRightX = nums1[partitionX] if partitionX != m else math.inf

            maxLeftY = nums2[partitionY - 1] if partitionY != 0 else -math.inf
            minRightY = nums2[partitionY] if partitionY != n else math.inf

            # Check if we have found the correct partition.
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # The partition is correct, now find the median.
                if total_length % 2 == 0:
                    # For an even number of total elements, the median is the average of the
                    # max of the left parts and the min of the right parts.
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    # For an odd number, the median is the max element of the left parts.
                    return float(max(maxLeftX, maxLeftY))
            
            # If the partition is not correct, adjust the binary search range.
            elif maxLeftX > minRightY:
                # The partitionX is too far to the right. Move left.
                high = partitionX - 1
            else:
                # The partitionX is too far to the left. Move right.
                low = partitionX + 1
        
        # This line should not be reached 

if inputs are sorted arrays.
        raise ValueError("Input arrays are not sorted.")