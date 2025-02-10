class Solution:
    def clearDigits(self, s: str) -> str:
        char = []
        for i in s:
            if ord(i)>=97 and ord(i)<=122:
                char.append(i)
            else:
                char.pop()
        
        return "".join(char)
    
