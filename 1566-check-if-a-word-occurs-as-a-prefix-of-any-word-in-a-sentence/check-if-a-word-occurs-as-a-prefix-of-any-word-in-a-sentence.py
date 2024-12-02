class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split(" ")
        ans=0
        for i in range(len(sentence)):
            if sentence[i][0:len(searchWord)] == searchWord:
                ans=i+1
                break
        return ans if ans>0 else -1