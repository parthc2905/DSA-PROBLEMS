class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l = ["qwertyuiop","asdfghjkl", "zxcvbnm"]
        state = 0 

        for i in range(len(words)):
            if words[i][0].lower() in l[0]:
                state = 0
            elif words[i][0].lower() in l[1]:
                state = 1
            else:
                state = 2
        
            for j in range(1,len(words[i])):
                if words[i][j].lower() not in l[state]:
                    words[i] = ""
                    break

        words = [i for i in words if i != '']

        return words
