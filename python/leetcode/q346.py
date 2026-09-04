from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.total = 0
