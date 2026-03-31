# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        # This buffer persists across different calls to read()
        self.queue = []

    def read(self, buf: List[str], n: int) -> int:
        idx = 0
        
        while idx < n:
            # If our internal queue is empty, we need to fetch from the file
            if not self.queue:
                buf4 = [''] * 4
                count = read4(buf4)
                
                # If read4 returns 0, we've hit EOF (End of File)
                if count == 0:
                    break
                
