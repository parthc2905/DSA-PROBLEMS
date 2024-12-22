class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        Map = {}
        used = []

        for x,y in zip(s,t):
            
            if x in Map:
                if Map[x] != y:
                    return False
            else:
                if y in used:
                    return False
            
            used.append(y)
            Map[x] = y
            
        return True
