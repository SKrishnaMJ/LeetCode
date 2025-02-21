class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        p1=0
        p2=0
        ct=0
        while(p2<len(t)):
            if p1<len(s) and s[p1]==t[p2]:
                p1+=1
                p2+=1
                ct+=1
            else:
                p2+=1
        return True if ct==len(s) else False


        
        