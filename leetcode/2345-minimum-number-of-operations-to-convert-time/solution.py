class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = current.split(":")
        correct = correct.split(":")
        diff = (int(correct[0])-int(current[0]))*60 + (int(correct[1])-int(current[1]))
        moves = diff//60 + (diff%60)//15 + ((diff%60)%15)//5 + ((diff%60)%15)%5

        return moves
