class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # convert to lower case and split string into words by spaces and punctuation
        a = re.split(r'\W+', paragraph.lower())
		
		# make new list consisitng of words not in banned list (remove banned words)
        b = [w for w in a if w not in banned and w !='']
		# return value that counted max times in the new list
        print(b)
        return max(b, key = b.count)
