class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        i=0
        summ=0
        for j in range(len(nums)):
            summ+=nums[j]
            while summ>=target:
                ans = min(ans, (j-i)+1)
                summ-=nums[i]
                i+=1
        return ans if ans!=float("inf") else 0

        