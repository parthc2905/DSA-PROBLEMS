class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row = len(grid)
        perimeter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    if (j>0 and grid[i][j-1]!=1) or (j==0):
                        perimeter+=1
                    if (j<col-1 and grid[i][j+1]!=1) or (j==col-1):
                        perimeter+=1
                    if (i>0 and grid[i-1][j]!=1) or (i==0):
                        perimeter+=1
                    if (i<row-1 and grid[i+1][j]!=1) or (i==row-1):
                        perimeter+=1
        return perimeter
                    
