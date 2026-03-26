class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        mini = float("inf")
        minj = float("inf")
        for i,j in ops:
            if mini>i:
                mini = i
            if minj>j:
                minj = j
        
        return mini*minj

            
