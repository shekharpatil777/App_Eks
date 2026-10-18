from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # Track the global bounding box
        min_x = min(r[0] for r in rectangles)
        min_y = min(r[1] for r in rectangles)
        max_x = max(r[2] for r in rectangles)
        max_y = max(r[3] for r in rectangles)

        # Track the total area of all sub-rectangles
        total_area = 0
        corners = set()

        for x1, y1, x2, y2 in rectangles:
            total_area += (x2 - x1) * (y2 - y1)

            # Four vertices of the current rectangle
            sub_corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
            for pt in sub_corners:
                if pt in corners:
                    corners.remove(pt)
                else:
                    corners.add(pt)

        # 1. Total area must equal the bounding box area
        expected_area = (max_x - min_x) * (max_y - min_y)
        if total_area != expected_area:
            return False
