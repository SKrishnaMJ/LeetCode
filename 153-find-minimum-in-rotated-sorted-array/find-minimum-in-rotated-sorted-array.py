class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums==nums.sort():
            return nums[0]
        ans=nums[0]
        for i in range(len(nums)-1,-1,-1):
            ans=min(ans, nums[i])
        return ans

        