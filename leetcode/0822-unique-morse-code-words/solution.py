class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        for word in range(len(words)):
            temp_str = ""
            for char in words[word]:
                temp_str += letters_code[ord(char)-97]
            words[word] = temp_str
        
        return len(set(words))
