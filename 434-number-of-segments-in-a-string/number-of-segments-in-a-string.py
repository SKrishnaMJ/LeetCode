class Solution:
    def countSegments(self, s: str) -> int:
        res=''
        ans=[]
        c=0
        for i in range(len(s)):
            if s[i] == " ":
                ans.append(res)
                res=''
                continue
            res+=s[i]
        ans.append(res)
        for j in ans:
            if j != "":
                c+=1
        return c
        