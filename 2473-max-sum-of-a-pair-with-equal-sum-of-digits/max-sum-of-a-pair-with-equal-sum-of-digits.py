class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res={}
        ans=-1
        for num in nums:
            s=0
            i=num
            while(i!=0):
                rem = i%10
                i = i//10
                s+=rem
            if s not in res:
                res[s]=num
            else:
                ans=max(ans,num+res[s])
                if num>res[s]:
                    res[s]=num
        return ans
        