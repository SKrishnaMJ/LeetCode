class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] == words[j][0:len(words[i])] and words[i] == words[j][len(words[j]) - len(words[i]):]:
                    cnt += 1
        return cnt

        