class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = map(str,digits)
        n = "".join(digits)
        n = int(n)
        n = n+1
        n = str(n)
        n = list(n)
        n = map(int,n)
        return n
