class Solution:
    def minSteps(self, n: int) -> int:
        cur=1
        copy=0
        ans=0
        while cur<n:
            if n%cur==0:
                copy=cur
                ans+=1
            ans+=1
            cur+=copy
        return ans


        