class Vector2D:

    def __init__(self, vec):
        self.vec = vec
        self.row = 0
        self.col = 0
        self._advance()

    def _advance(self):
        while self.row < len(self.vec) and self.col >= len(self.vec[self.row]):
            self.row += 1
            self.col = 0
