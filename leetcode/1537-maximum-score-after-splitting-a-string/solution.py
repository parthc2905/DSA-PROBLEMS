class Solution:
    def maxScore(self, s: str) -> int:
        max_val = 0
        for i in range(len(s)-1):
            max_val = max(max_val, s[:i+1].count('0')+s[i+1:].count('1'))
        
        return max_val
