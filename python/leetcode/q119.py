class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        

        for k in range(rowIndex):
            next_val = row[-1] * (rowIndex - k) // (k + 1)
            row.append(next_val)
        
        return row
