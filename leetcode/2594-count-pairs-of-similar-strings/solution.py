class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words = [set(i) for i in words]
        c = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i]==words[j]:
                    c+=1
        return c
