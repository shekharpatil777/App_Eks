from collections import deque

class ZigzagIterator:
    def __init__(self, v1: list[int], v2: list[int]):
        # Store tuples of (vector, current_index) in a queue
        # Only add vectors that are not empty
        self.queue = deque()
        if v1:
            self.queue.append((v1, 0))
        if v2:
            self.queue.append((v2, 0))

    def next(self) -> int:
        if not self.hasNext():
            raise Exception("No more elements")
        
        # Get the vector at the front of the queue
        vec, idx = self.queue.popleft()
        val = vec[idx]
        
        # If the vector still has remaining elements, put it back at the end
        if idx + 1 < len(vec):
            self.queue.append((vec, idx + 1))
            
        return val

    def hasNext(self) -> bool:
        return len(self.queue) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())