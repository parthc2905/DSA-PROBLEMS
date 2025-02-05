class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first_index_diff = 0
        second_index_diff = 0
        c = 0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                c+=1
                if c > 2:
                    return False
                elif c == 1:
                    # store the index of first difference
                    first_index_diff = i
                else:
                    # store the index of second difference
                    second_index_diff = i
        return (s1[first_index_diff] == s2[second_index_diff] and s1[second_index_diff] == s2[first_index_diff])
