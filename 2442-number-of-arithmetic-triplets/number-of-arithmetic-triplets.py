class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ctr=0
        for i in nums:
            if (i+diff in nums and i+(diff*2) in nums):
                ctr+=1
        return ctr
        