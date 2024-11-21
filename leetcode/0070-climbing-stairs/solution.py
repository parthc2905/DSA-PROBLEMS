class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        l = 0
        if n == 1:
            return 1
        else:
            for i in range(n-1):
                l = a+b
                a = b
                b = l
            return l
