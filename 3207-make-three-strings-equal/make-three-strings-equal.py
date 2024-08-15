class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        ctr=0
        if s1[0]!=s2[0] or s3[0]!=s2[0] or s1[0]!=s3[0]:
            return -1

        for i in range(min(len(s1),len(s2),len(s3))):
            if(s1[i]==s2[i] and s2[i]==s3[i] and s3[i]==s1[i]):
                ctr+=1
            else:
                break
        return ((len(s1)-ctr)+(len(s2)-ctr)+(len(s3)-ctr))
        