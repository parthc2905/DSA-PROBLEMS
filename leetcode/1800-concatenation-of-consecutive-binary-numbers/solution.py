class Solution:
    def concatenatedBinary(self, n: int) -> int:
        sumBin = ''
        for i in range(1,n+1):
            sumBin += bin(i)[2:]
        return int(sumBin,2)%(10**9+7)
