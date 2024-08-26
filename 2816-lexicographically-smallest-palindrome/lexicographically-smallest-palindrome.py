class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        t=s[::-1]
        res=''
        for i in range(len(s)):
            if s[i]!=t[i] and s[i]>t[i]:
                res+=t[i]
            elif s[i]!=t[i] and s[i]<t[i]:
                res+=s[i]
            else:
                res+=s[i]
        return res
        