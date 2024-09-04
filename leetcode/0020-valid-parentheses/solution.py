class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if not stack or d[i] != stack.pop():
                    return False

        return not stack
        
