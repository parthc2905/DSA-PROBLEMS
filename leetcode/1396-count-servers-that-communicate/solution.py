class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        numrows = len(grid[0])
        numcols = len(grid)
        rows = [0]*numrows
        cols = [0]*numcols
        
        for i in range(numcols):
            for j in range(numrows):
                if grid[i][j]:
                    rows[j] += 1
                    cols[i] += 1
        
        count = 0
        for i in range(numcols):
            for j in range(numrows):
                if grid[i][j]:
                    if rows[j]>1 or cols[i]>1:
                        count+=1
        
        return count
