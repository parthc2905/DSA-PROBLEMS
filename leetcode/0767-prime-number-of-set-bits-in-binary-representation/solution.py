class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = [2, 3, 5, 7, 11, 13, 17 , 19]
        variable = 0
        for value in range(left,right+1):
            if bin(value).count("1") in prime:
                variable += 1
        
        return variable
