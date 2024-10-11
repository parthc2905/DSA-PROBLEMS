class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)
        i = 0
        while(i<len(s)):
            l[i:i+k] = l[i:k+i][::-1]
            i += k*2

        return "".join(l)

        
        
            
