import random

class Solution:

    def __init__(self, head):
        self.head = head

    def getRandom(self) -> int:
        current = self.head
        result = 0
        count = 0

        while current:
            count += 1
