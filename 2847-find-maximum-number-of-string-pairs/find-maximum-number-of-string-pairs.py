class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ctr=0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if(words[i] == words[j][::-1]):
                    ctr+=1
        return ctr


        