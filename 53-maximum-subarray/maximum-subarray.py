class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=float("-inf")
        tot=0
        for i in range(len(nums)):
            tot+=nums[i]
            ans=max(ans,tot)
            if tot < 0:
                tot=0
        return ans