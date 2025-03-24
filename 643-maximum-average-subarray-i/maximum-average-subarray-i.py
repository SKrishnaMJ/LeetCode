class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=0
        for i in range(k):
            summ+=nums[i]
        ans=summ/k
        for j in range(k, len(nums)):
            summ+=nums[j]
            summ-=nums[j-k]
            ans=max(ans, summ/k)
        return ans

