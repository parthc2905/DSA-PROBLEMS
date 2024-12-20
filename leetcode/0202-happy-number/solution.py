class Solution:
    def isHappy(self, n: int) -> bool:
        st = set()
        flag=1
        while (flag==1):
            squareSum = 0
            while (n != 0):
                squareSum += (n % 10) ** 2
                n = n // 10
            n=squareSum
            if (n == 1):
                return True
            if n in st:
                flag=0
            st.add(n)
        if(flag==1):
            return True
        else:
            return False     
