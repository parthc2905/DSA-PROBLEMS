class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        numrows, numcols = len(mat),len(mat[0])
        rows, cols = [0]*numrows , [0]*numcols
        nums_to_pos = {}
        for row in range(numrows):
            for col in range(numcols):
                nums_to_pos[mat[row][col]] = [row,col]
        
        for i in range(len(arr)):
            num = arr[i]
            row,col = nums_to_pos[num]
            
            rows[row]+=1
            cols[col]+=1

            if rows[row] == numcols or cols[col] == numrows:
                return i
        
        return -1
