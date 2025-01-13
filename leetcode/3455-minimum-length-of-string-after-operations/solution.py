from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        s = 0
        for i,j in c.items():
            if j>2:
                if j%2:
                    s+=1
                else:
                    s+=2
            else:
                s+=j
        
        return s
