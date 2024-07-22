class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        if len(s) == 1 and s in t:
            return True
        fp=0
        ctr=0
        for i in t:
            if(s[fp]==i):
                ctr+=1
                fp+=1
                if(fp==len(s)):
                    break
        if(ctr==len(s)):
            return True
        else:
            return False

        