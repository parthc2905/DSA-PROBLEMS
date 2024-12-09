class Solution:
    def fib(self, n: int) -> int:
        # if (n==0 ):
        #     return 0
        # elif (n==1):
        #     return 1
        # else:
        #     return self.fib(n-1) + self.fib(n-2)
        f1 = 0
        f2 = 1
        if (n==0):
            return f1
        elif (n==1):
            return f2
        else:
            s = 0
            for i in range(1,n):
                s = f1+f2
                f1 = f2
                f2 = s
            
            return s
