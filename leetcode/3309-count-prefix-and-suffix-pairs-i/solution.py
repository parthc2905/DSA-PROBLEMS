class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)
        for i in range(n):
            l1 = len(words[i])
            for j in range(i+1,n):
                l2 = len(words[j])
                if l1<=l2:
                    if words[i] == words[j][:l1] and words[i]==words[j][l2-l1:]:
                        count+=1
        
        return count
