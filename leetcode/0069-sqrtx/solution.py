class Solution:
    def mySqrt(self, x: int) -> int:
        # 1,4,9,16,25,36,49
        # 3,5,7,9,11, 2n+1
        i = 0
        s = (2*i+1)
        while(x>=s):
            i+=1
            s+= (2*i+1)
        
        return i


        
