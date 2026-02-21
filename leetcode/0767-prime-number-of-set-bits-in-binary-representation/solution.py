import math
class Solution(object):
    def countPrimeSetBits(self, left, right):
        prime = [2, 3, 5, 7, 11, 13, 17 , 19]
        variable = 0
        for value in xrange(left,right+1):
            if bin(value).count("1") in prime:
                variable += 1
        
        return variable
        

    #     setbits = []
    #     for value in xrange(left,right+1):
    #         setbits.append(bin(value).count("1"))
        
    #     variable = 0
    #     for i in setbits:
    #         if self.is_prime(i) and i!=1:
    #             variable+=1
        
    #     return variable

    # def is_prime(self, number):

    #     for i in xrange(2,int(math.sqrt(number))+1):
    #         if number%i == 0:
    #             return 0
        
    #     return 1
        
