class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [] # Stores indices: (index, height)
        max_area = 0
        
        # We add a 0 at the end to ensure we pop everything 
        # out of the stack at the finish.
        heights.append(0)
        
        for i, h in enumerate(heights):
            start = i
            # While the current height is shorter than the top of the stack
            while stack and stack[-1][1] >= h:
                index, height = stack.pop()
                # Calculate area with the popped height as the shortest bar
                max_area = max(max_area, height * (i - index))
                # The 'start' for the current bar moves back to the popped index
                start = index
            
            stack.append((start, h))
            
        return max_area