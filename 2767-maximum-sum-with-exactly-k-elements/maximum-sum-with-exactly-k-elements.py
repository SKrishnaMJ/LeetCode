class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:

        s=0
        for i in range(k):
            r=max(nums)
            s+=r
            nums.append(r+1)
        return s
        