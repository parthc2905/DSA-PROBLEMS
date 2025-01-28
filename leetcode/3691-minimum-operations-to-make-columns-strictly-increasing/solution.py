class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        operation = 0
        for col in range(len(grid[0])):
            pre = grid[0][col]
            for row in range(1,len(grid)):
                curr = grid[row][col]
                if pre>=curr:
                    operation += (pre-curr+1)
                    grid[row][col] = (pre+1)
                pre = grid[row][col]
        
        return operation
