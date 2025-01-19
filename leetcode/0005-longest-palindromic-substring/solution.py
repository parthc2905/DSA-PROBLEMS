class Solution:
    def isPalidrome(self, string: str):
        if len(string)%2==0:
            if string[:len(string)//2] != string[:len(string)//2-1:-1]:
                return False
        else:
            if string[:len(string)//2] != string[:len(string)//2:-1]:
                return False
        return True
    
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s),0,-1):
            for j in range(len(s)-i+1):
                if self.isPalidrome(s[j:j+i]):
                    return s[j:j+i]
        return ""
    
    
