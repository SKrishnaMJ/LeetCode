class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        c=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                c.append(i)
        if len(c)==2:
            i,j=c
            return s1[i]==s2[j] and s1[j]==s2[i]
        return False
