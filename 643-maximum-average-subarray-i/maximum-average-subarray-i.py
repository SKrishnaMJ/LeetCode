class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        res = curr_sum
        for i in range(k,len(nums)):
            curr_sum+=nums[i] - nums[i-k]
            res = max(res,curr_sum)
        return res/k