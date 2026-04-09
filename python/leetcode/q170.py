class TwoSum:
    def __init__(self):
        # Dictionary to store number counts
        self.num_counts = {}

    def add(self, number: int) -> None:
        # Increment count if exists, else set to 1
        self.num_counts[number] = self.num_counts.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for num in self.num_counts:
            target = value - num
            
