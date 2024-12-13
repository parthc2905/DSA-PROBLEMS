from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        l_count = {}
        for i in licensePlate.lower():
            if ord(i)>=97 and ord(i)<=122:
                if i in l_count:
                    l_count[i] +=1
                else:
                    l_count[i] = 1
        fetched_list = []
        minLen = float("inf")
        for i in words:
            count = Counter(i)
            for j in l_count.keys():
                if j in count:
                    if l_count[j] >count[j]:
                        break
                else:
                    break
            else:
                fetched_list.append((i,len(i)))
                minLen = min(minLen,len(i))
        

        
        for i,j in fetched_list:
            if j == minLen:
                return i
