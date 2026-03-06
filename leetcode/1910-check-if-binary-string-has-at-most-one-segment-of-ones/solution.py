class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # count = s.count('1')
        # for i in range(len(s)):
        #     if s[i]!='1' and count:
        #         return False
        #     if count == 0:
        #         return True
        #     count-=1
        # return True
        return "01" not in s
