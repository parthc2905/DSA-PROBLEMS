class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = []
        for i in operations:
            if i=="+":
                val = l[-1]+l[-2]
                l.append(val)
            elif i=="D":
                val = l[-1]*2
                l.append(val)
            elif i=="C":
                l.pop()
            else:
                l.append(int(i))
        
        return sum(l)
