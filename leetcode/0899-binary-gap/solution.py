class Solution:
    def binaryGap(self, n: int) -> int:
        bits = bin(n)[2:]
        prev = 0
        dist = 0
        for curr in range(len(bits)):
            if bits[curr] == "1" :
                if dist < curr-prev:
                    dist = curr-prev
                prev = curr
    
        return dist

