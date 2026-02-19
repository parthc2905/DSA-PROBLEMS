class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n^=(n>>1)
        
        if (n & (n+1)) == 0:
            return True 

        return False 
