# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         d = {}
#         for i in s:
#             if i in d:
#                 d[i] +=1
#             else:
#                 d[i] = 1
        
#         for i in t:
#             if i in d and d[i]!=0:
#                 d[i]-=1
#             else:
#                 return False
        
#         for i,j in d.items():
#             if j!=0:
#                 return False
        
#         return True

class Solution(object):
    def isAnagram(self, s, t):
        if(len(s) != len(t)): return False
        myHash = set()
        for i in range(len(t)):
         if(s[i] in myHash):continue
         if s.count(s[i]) != t.count(s[i]): return False
         myHash.add(s[i])
        return True
