class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans=0
        pr_sum, pr_sum_rev = [0]*len(nums),[0]*len(nums)
        for i in range(len(nums)-1):
            pr_sum[i+1] = pr_sum[i] + nums[i]
        for j in range(len(nums)-1,-1,-1):
            pr_sum_rev[j-1] = pr_sum_rev[j] + nums[j]
        for k in range(len(nums)-1):
            if pr_sum[k+1] >= pr_sum_rev[k]:
                ans+=1
        return ans
        