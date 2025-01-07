class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # l = []
        # words.sort(key=len)
        # for i in range(len(words)):
        #     for j in range(i+1,len(words)):
        #         if words[i] in words[j] and words[i] not in l:
        #             l.append(words[i])
        # return l

        r=' '.join(words)
        s=[i for i in words if r.count(i)>1]
        return s
