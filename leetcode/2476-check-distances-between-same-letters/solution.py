class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # use = []

        # for c in range(len(s)):
        #     if s[c] not in use:
        #         use.append(s[c])
        #         if distance[ord(s[c])-97]+c+1>=len(s) or (distance[ord(s[c])-97]+1<len(s) and s[c] != s[distance[ord(s[c])-97]+c+1]) :
        #             return False
        #     else:
        #         use.remove(s[c])
        
        # return True

        first = {}
        for i, c in enumerate(s):
            if c in first:
                if distance[ord(c) - ord('a')] != i - first[c] - 1:
                    return False
            first[c] = i
        return True
