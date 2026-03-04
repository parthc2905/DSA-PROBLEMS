class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # icoor = []
        # jcoor = []
        # l = 0
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if mat[i][j]:
        #             icoor.append(i)
        #             jcoor.append(j)
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if mat[i][j]:
        #             if icoor.count(i) == 1 and jcoor.count(j) == 1:
        #                 l+=1
        # return l

        # anothers code
        def get_column_sum(col_idx):
            return sum(row[col_idx] for row in mat)

        special = 0
        for row in mat:
            if sum(row) == 1:
                col_idx = row.index(1)
                special += get_column_sum(col_idx) == 1

        return special
