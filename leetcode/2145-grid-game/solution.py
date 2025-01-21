class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        minimize = float('inf')
        first_row_sum = sum(grid[0])
        sec_row_sum = 0

        for i in range(len(grid[0])):
            first_row_sum -= grid[0][i]
            minimize = min(minimize,max(first_row_sum,sec_row_sum))
            sec_row_sum += grid[1][i]
        
        return minimize
