class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        diffch=''
        if(len(word2)>len(word1)):
            diff=len(word2)-len(word1)
            diffch=word2[len(word2)-diff:]
        elif(len(word1)>len(word2)):
            diff=len(word1)-len(word2)
            diffch = word1[len(word1) - diff:]
        l=min(len(word1),len(word2))
        res=''
        for i in range(l):
            res=res+word1[i]+word2[i]
        return res+diffch

        