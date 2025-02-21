class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=''
        n=len(word1)
        m=len(word2)
        for i in range(min(n,m)):
            merged+=word1[i]+word2[i]
        if m>n:
            return merged+word2[n:]
        else:
            return merged+word1[m:]
        