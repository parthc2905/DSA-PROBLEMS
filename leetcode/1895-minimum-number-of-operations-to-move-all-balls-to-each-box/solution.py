class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = []
        l = []
        for i in range(n):
            if boxes[i] == '1':
                l.append(i)
        
        for i in range(n):
            s = 0
            for j in l:
                s+=abs(i-j)
            answer.append(s)

        return answer
