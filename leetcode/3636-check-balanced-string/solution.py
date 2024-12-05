class Solution:
    def isBalanced(self, num: str) -> bool:
        esum = 0
        osum = 0
        for i in range(len(num)):
            if i%2 == 0:
                osum+=int(num[i])
            else:
                esum+=int(num[i])
        
        if esum==osum:
            return True
        else:
            return False
