class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        if (haystack==needle or needle==""):
            return 0
        while (i<len(haystack)) and (needle in haystack):
            j = 0
            c = 0
            if haystack[i]==needle[0]:
                while(j<len(needle)):
                    if haystack[i+j]==needle[j]:
                        c+=1
                    j+=1
                if c == len(needle):
                    return i
            i+=1

        return -1
