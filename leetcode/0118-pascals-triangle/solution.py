class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []

        for i in range(1,numRows+1):
            l = []
            k = 0
            for j in range(i):
                if j == 0 or j == i-1:
                    l.append(1)
                else:
                    l.append(pascal[i-2][k]+pascal[i-2][k+1])
                    k+=1
            pascal.append(l)

        return pascal
