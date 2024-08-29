class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        while(len(nums)!=0):
            i,j = nums.pop(0), nums.pop(len(nums)-1)
            ans=max(ans, i+j)
        return ans
        