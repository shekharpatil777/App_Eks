from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n
        
        result = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicate = 1
            
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                if x1 == x2 and y1 == y2:
                    duplicate += 1
                else:
                    dx = x2 - x1
                    dy = y2 - y1
                    
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g
                    
                    slopes[(dx, dy)] += 1
            
