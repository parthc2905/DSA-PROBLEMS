class Solution:
    def minOperations(self, s: str) -> int:
        poss = ['01'*(len(s)//2)+ ('0' if len(s)%2 else '') ,'10'*(len(s)//2) + ('1' if len(s)%2 else '')]
        mini = 123456789012345678901234567890
        for string in poss:
            count = 0
            for i in range(len(s)):
                if s[i]!=string[i]:
                    count+=1
            
            mini = min(mini,count)
            
        return mini
