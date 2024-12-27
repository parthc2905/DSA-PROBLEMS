from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = Counter(s)
        PaliLen = 0
        odd = 0
        for c in s.values(): 
            if c%2 == 0:
                PaliLen +=c
            else:
                PaliLen += (c-1)
                odd = 1
        return PaliLen + odd
