class Solution:
    def tribonacci(self, n: int) -> int:
        f0 = 0
        f1 = 1
        f2 = 1
        if n==0:
            return f0
        elif n==1:
            return f1
        elif n==2:
            return f2
        else :
            s = 0
            for i in range(2,n):
                s = f0 + f1 + f2
                f0 = f1
                f1 = f2 
                f2 = s
            return s
