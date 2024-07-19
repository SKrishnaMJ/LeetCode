class Solution:
    def longestNiceSubstring(self, s: str) -> str:


        # ans=''
        # res=''
        # if(len(s)<=1):
        #     return ""
        # for i in range(len(s)-1):
        #     tem=s[i]
        #     if s[i].islower() and s[i+1] == tem.upper() or s[i].isupper() and s[i+1] == tem.lower():
        #         for j in range(i,len(s)):
        #             if (s[j] == tem.lower() or s[j] == tem.upper()):
        #                 ans=ans+s[j]
        #         if(len(ans) > len(res)):
        #             res=ans
        #             ans=''
        #         elif(s.index(res[-1])+1)==s.index(ans[0]):
        #             res=res+ans
        # return res
        n=len(s)
        best=""

        for i in range(n):
            for j in range(i,n):
                sub=s[i:j+1]
                if all(ch.upper() in sub and ch.lower() in sub for ch in sub):
                    best=max(best,sub,key=len)

        return best



        