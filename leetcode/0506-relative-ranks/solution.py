class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = []
        s = sorted(score, reverse=True)
        for i in score:
            j = s.index(i)
            if j == 0:
                ranks.append("Gold Medal")
            elif j == 1:
                ranks.append("Silver Medal")
            elif j == 2:
                ranks.append("Bronze Medal")
            else:
                ranks.append(f"{j+1}")
        return ranks
