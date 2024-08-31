class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftSum=[0]*n
        rightSum=[0]*n
        numsNew=nums[::-1]
        ans=[0]*n
        for i in range(1,n):
            leftSum[i]=leftSum[i-1]+nums[i-1]
            rightSum[i]=rightSum[i-1]+numsNew[i-1]
        rightSum=rightSum[::-1]
        for i in range(n):
            ans[i]=abs(leftSum[i]-rightSum[i])
        return ans
        


        