class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = sorted(nums)
        # if len(nums) == 2 and 2 not in nums:
        #     return 2
        if len(nums) not in nums:
            return len(nums)
        for i in range(len(a)):
            if i != a[i]:
                return i 
        