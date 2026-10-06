from collections import deque


class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.queue = deque(range(maxNumbers))
        self.is_available = [True] * maxNumbers

    def get(self) -> int:
        if not self.queue:
            return -1
        number = self.queue.popleft()
        self.is_available[number] = False
        return number

    def check(self, number: int) -> bool:
        return self.is_available[number]
