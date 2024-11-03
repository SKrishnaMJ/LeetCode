class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l=sentence.split(" ")
        f=l[0][0]
        if f==l[-1][len(l[-1])-1]:

            la=l[0][len(l[0])-1]
            for i in range(1,len(l)):
                if la != l[i][0]:
                    return False
                else:
                    la=l[i][len(l[i])-1]
            return True
        else:
            return False
        