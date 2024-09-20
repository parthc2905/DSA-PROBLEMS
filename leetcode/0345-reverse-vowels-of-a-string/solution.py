class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s)-1
        l = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        while(i<j):
            if s[i].lower() in l and s[j].lower() in l:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
            
            if s[i].lower() not in l:
                i+=1
            if s[j].lower() not in l:
                j-=1
        
        s = "".join(s)
        return s

