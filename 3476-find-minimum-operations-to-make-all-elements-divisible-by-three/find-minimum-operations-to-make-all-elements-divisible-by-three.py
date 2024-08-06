class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ctr=0
        for i in nums:
            if i%3==0:
                ctr+=1
        return len(nums)-ctr
        