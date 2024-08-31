class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l=0
        r=0
        for i in range(len(nums)):
            l+=nums[i]
            r=sum(nums[i:])
            if l==r:
                return i
        return -1
        #     for j in range(i, len(nums)):
        #         r+=nums[j]
        #     if l==r:
        #         return i
        #     else:
        #         r=0
        # return -1
        