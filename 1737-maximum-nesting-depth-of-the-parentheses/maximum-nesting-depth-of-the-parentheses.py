class Solution:
    def maxDepth(self, s: str) -> int:
        ctr, ans = 0, 0
        l=[]
        for i in range(len(s)):
            if s[i] == ')':
                l.pop()
                ctr-=1
            elif s[i] == '(':
                l.append(s[i])
                ctr+=1
            ans=max(ans,ctr)
        return ans

        