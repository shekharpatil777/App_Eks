class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        
        def backtrack(start, current_path):
            # Base case: if the combination is the right length, save it
            if len(current_path) == k:
                result.append(list(current_path))
                return
            
            # Iterate through the numbers from 'start' to 'n'
            # Optimization: n - (k - len(current_path)) + 2 ensures 
            # we don't start loops that can't possibly finish a full k-length set
            for i in range(start, n + 1):
                # 1. Choose the number
                current_path.append(i)
                
                # 2. Explore further by moving to the next number
                backtrack(i + 1, current_path)
                
                # 3. Backtrack (remove the number) to try the next possibility
                current_path.pop()
        
        backtrack(1, [])
        return result