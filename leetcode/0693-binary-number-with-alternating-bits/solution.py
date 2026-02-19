class Solution(object):
    def hasAlternatingBits(self, n):
        bits = bin(n)
        for i in xrange(2,len(bits)-1):
            if bits[i] == bits[i+1]:
                return False
        
        return True

        
