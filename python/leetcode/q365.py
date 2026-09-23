from collections import deque


class Solution:

  def canMeasureWater(self, x: int, y: int, target: int) -> bool:
    if target > x + y:
      return False

    # State: (jug1_water, jug2_water)
    queue = deque([(0, 0)])
    visited = {(0, 0)}

    while queue:
      a, b = queue.popleft()

      if a == target or b == target or a + b == target:
        return True

      # All 6 possible next states:
      next_states = {
          (x, b),  # Fill jug 1
          (a, y),  # Fill jug 2
          (0, b),  # Empty jug 1
          (a, 0),  # Empty jug 2
          (
              a - min(a, y - b),
              b + min(a, y - b),
          ),  # Pour jug 1 -> jug 2
          (
              a + min(b, x - a),
              b - min(b, x - a),
          ),  # Pour jug 2 -> jug 1
      }
