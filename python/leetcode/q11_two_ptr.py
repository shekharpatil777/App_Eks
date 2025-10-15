#Find two lines that together with the x-axis form a container that holds the most water.
Return the maximum area of water the container can store.
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)

            # Move the pointer at the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
