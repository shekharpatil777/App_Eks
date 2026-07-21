from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        result = []

        for i in range(len(currentState) - 1):
            if currentState[i:i + 2] == "++":
                next_state = (
                    currentState[:i]
                    + "--"
                    + currentState[i + 2:]
                )
                result.append(next_state)

        return result