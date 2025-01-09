class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        l = len(pref)
        for i in words:
            if pref==i[:l]:
                count+=1
        return count
