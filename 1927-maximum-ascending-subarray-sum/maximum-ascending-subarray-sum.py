class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res=[]
        ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                res.append(ans)
                ans=nums[i]
            else:
                ans+=nums[i]
        res.append(ans)
        return max(res)
        