class Solution:
    def findTheDifference(self, s: str, t: str):
        for i in s:
            t = t.replace(i,"",1)
        return t
