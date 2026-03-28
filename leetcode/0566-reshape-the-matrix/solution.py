class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if ((cols*rows)!=(c*r) )  :
            return mat
        reshape = [[0]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                idx = i * c + j
                reshape[i][j] = mat[idx // cols][idx % cols]
        return reshape
