class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        ans=0
        res=0
        while(len(satisfaction)>0):
            for i in range(len(satisfaction)):
                ans+=(satisfaction[i]*(i+1))
            if ans < 0:
                satisfaction=satisfaction[1:]
                res=ans
                ans=0
            else:
                res=max(res,ans)
                ans=0
                satisfaction = satisfaction[1:]
        if res>0:
            return res
        else:
            return 0

        