class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res, cur, num_of_letters = [], [], 0
        
        for w in words:
            # Check if adding this word exceeds maxWidth
            # len(cur) represents the minimum 1 space between words
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # Distribute spaces
                for i in range(maxWidth - num_of_letters):
                    # Modular arithmetic handles the "left-heavy" space distribution
                    # If only 1 word, i % 1 is always 0, putting all spaces after it
                    cur[i % (len(cur) - 1 or 1)] += ' '
                
                res.append("".join(cur))
                cur, num_of_letters = [], 0
            
            cur.append(w)
            num_of_letters += len(w)
            
