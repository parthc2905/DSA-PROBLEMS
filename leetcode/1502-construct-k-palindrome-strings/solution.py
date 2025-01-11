class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        d = {}
        if len(s)<k:
            return False
        if len(s)==k:
            return True
        odd = 0
        hashmap = set()
        for i in s:
            if i not in hashmap:
                if s.count(i)%2:
                    odd+=1
                hashmap.add(i)
        return odd<=k
