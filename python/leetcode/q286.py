from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return

        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        # Add all gates to the queue.
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    queue.append((row, col))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
