class NestedIterator:
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        self._flatten()
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        self._flatten()
        return len(self.stack) > 0
