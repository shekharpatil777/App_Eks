from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)

        # Add original values as leaf nodes
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]

        # Build parent nodes
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        position = index + self.n
        self.tree[position] = val

        # Update all parent nodes
        while position > 1:
            position //= 2
            self.tree[position] = (
                self.tree[2 * position]
                + self.tree[2 * position + 1]
            )

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n

        total = 0
